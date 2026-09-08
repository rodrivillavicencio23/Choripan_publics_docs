# ------------------------------
# Imports y Modularización
import socket
import threading
import json
from datetime import datetime
from pathlib import Path
from parametros import (
    HOST, PORT, MAX_LISTEN,
    ENCODING, USUARIOS_CSV, GANANCIAS_CSV,
    SPECIAL_USERS, SALDO_INICIAL, SALDO_ESPECIAL
)

# ------------------------------
# ------- MANEJO JSON csv's ----
def ensure_json_csv(path, default_data):
    """
    Crea un archivo .csv (JSON real) si no existe o si está corrupto.
    Si el archivo existe pero está corrupto, hace una copia .bak y reescribe con default_data.
    """
    p = Path(path)
    if not p.exists():
        with p.open("w", encoding="utf-8") as f:
            json.dump(default_data, f, indent=4)
        return

    # si existe, comprobar que contiene JSON válido y no está vacío
    try:
        content = p.read_text(encoding="utf-8").strip()
        if not content:
            # archivo vacío -> inicializar
            with p.open("w", encoding="utf-8") as fw:
                json.dump(default_data, fw, indent=4)
            return
        # intentar parsear
        json.loads(content)
    except Exception:
        # respaldo y reescritura
        try:
            backup = p.with_suffix(p.suffix + ".bak")
            p.replace(backup)
            print(f"[WARN] Archivo {path} corrupto. Se creó copia de seguridad: {backup}")
        except Exception:
            print(f"[WARN] No se pudo crear backup de {path}")
        with p.open("w", encoding="utf-8") as fw:
            json.dump(default_data, fw, indent=4)


def load_json_csv(path, default_data=None):
    """
    Lee JSON desde path. Si falla devuelve default_data (o un sensible)
    y re-inicializa el archivo.
    """
    p = Path(path)
    if not p.exists():
        if default_data is None:
            default_data = {}
        ensure_json_csv(path, default_data)
        return default_data

    try:
        with p.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[WARN] Error leyendo {path}: {e}. Re-inicializando archivo.")
        if default_data is None:
            default_data = {}
        ensure_json_csv(path, default_data)
        return default_data


def save_json_csv(path, data):
    p = Path(path)
    with p.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


# Crear usuarios.csv y ganancias.csv si no existen o están corruptos
ensure_json_csv(USUARIOS_CSV, {"usuarios": []})
ensure_json_csv(GANANCIAS_CSV, {"ganancias": []})


# ------------------------------
# --- FUNCIONES DE USUARIOS -----
def get_user_record(username):
    """
    Devuelve el usuario desde usuarios.csv.
    Si NO existe, lo crea con SALDO_INICIAL o SALDO_ESPECIAL.
    Siempre devuelve un dict válido.
    """
    data = load_json_csv(USUARIOS_CSV, default_data={"usuarios": []})
    usuarios = data.get("usuarios", [])

    # Buscar existente
    for u in usuarios:
        if u.get("username") == username:
            # Si es un usuario antiguo sin fecha, la agregamos
            if "fecha_creacion" not in u:
                u["fecha_creacion"] = datetime.now().isoformat()
                save_json_csv(USUARIOS_CSV, data)
            return u

    # No existe → crear
    saldo = SALDO_ESPECIAL if username in SPECIAL_USERS else SALDO_INICIAL
    nuevo = {
        "username": username,
        "saldo": saldo,
        "fecha_creacion": datetime.now().isoformat()
    }

    usuarios.append(nuevo)
    data["usuarios"] = usuarios
    save_json_csv(USUARIOS_CSV, data)

    print(f"[DB] Usuario nuevo creado: {username} con saldo {saldo}")
    return nuevo



def set_user_balance(username, new_amount):
    data = load_json_csv(USUARIOS_CSV, default_data={"usuarios": []})
    usuarios = data.get("usuarios", [])
    for u in usuarios:
        if u.get("username") == username:
            u["saldo"] = new_amount
            data["usuarios"] = usuarios
            save_json_csv(USUARIOS_CSV, data)
            return
    # si no existe, crearlo
    usuarios.append({"username": username, "saldo": new_amount})
    data["usuarios"] = usuarios
    save_json_csv(USUARIOS_CSV, data)


# ---------------------------------------------------------


class Server:
    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = port

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(MAX_LISTEN)

        self.active_users = set()
        self.threads = []
        self.running = True

        print(f"[INFO 151] Servidor escuchando en localhost:{self.port}")


    # -------------------------------------------------
    def handle_client(self, conn, addr):
        print(f"[INFO] Cliente conectado desde {addr}")

        username = None

        try:
            # 1) Handshake
            conn.sendall("HANDSHAKE NOMBRE\n".encode())

            raw = conn.recv(1024)
            if not raw:
                conn.close()
                return

            msg = raw.decode().strip()
            if not msg.startswith("USERNAME "):
                conn.sendall("ERROR PROTOCOLO\n".encode())
                conn.close()
                return

            username = msg.split(" ", 1)[1]

            # 2) Evitar duplicados
            if username in self.active_users:
                conn.sendall("ERROR NOMBRE_EN_USO\n".encode())
                conn.close()
                return

            # 3) Registrar usuario en memoria
            self.active_users.add(username)

            # 4) Crear o cargar desde BD (defensivo)
            user_rec = get_user_record(username)
            print(f"[OK] Usuario '{username}' conectado con saldo {user_rec.get('saldo')}")

            # 5) Confirmación
            conn.sendall(f"WELCOME {username}\n".encode())

            # 6) LOOP de mensajes --------------------
            while True:
                raw = conn.recv(4096)
                if not raw:
                    break

                msg = raw.decode().strip()
                print(f"[{username}] -> {msg}")

                # ------ GET_BALANCE ------
                if msg.startswith("GET_BALANCE"):
                    parts = msg.split()
                    if len(parts) != 2:
                        conn.sendall("ERROR PROTOCOLO\n".encode())
                        continue

                    user = parts[1]
                    rec = get_user_record(user)
                    saldo = rec.get("saldo", 0)

                    conn.sendall(f"BALANCE {saldo}\n".encode())
                    continue

                # ------ SET_BALANCE (opcional) ------
                if msg.startswith("SET_BALANCE"):
                    try:
                        _, user, amount = msg.split()
                        amount = float(amount)
                        set_user_balance(user, amount)
                        conn.sendall(f"OK SET_BALANCE {user}\n".encode())
                    except Exception:
                        conn.sendall("ERROR SET_BALANCE\n".encode())
                    continue

                # ------ LOGOUT ------
                if msg.startswith("LOGOUT"):
                    break

                # Otros comandos podrían ir aquí

        except Exception as e:
            print(f"[ERROR] handle_client: {e}")

            # intentar notificar al cliente antes de cerrar
            try:
                conn.sendall(f"ERROR SERVER {str(e)}\n".encode())
            except Exception:
                pass

        finally:
            if username and username in self.active_users:
                self.active_users.remove(username)
            try:
                conn.close()
            except Exception:
                pass
            print(f"[INFO] Usuario '{username}' desconectado")


    # -------------------------------------------------
    def start(self):
        try:
            while self.running:
                conn, addr = self.server_socket.accept()

                thread = threading.Thread(
                    target=self.handle_client,
                    args=(conn, addr),
                    daemon=True
                )
                thread.start()
                self.threads.append(thread)

                print(f"[INFO] Hilo iniciado para {addr}")

        except KeyboardInterrupt:
            print("\n[INFO 151] Deteniendo servidor...")
            self.shutdown()
        except Exception as error:
            print(f"[ERROR] Error en server loop: {error}")
            self.shutdown()


    # -------------------------------------------------
    def shutdown(self):
        self.running = False
        try:
            self.server_socket.close()
        except:
            pass

        for t in self.threads:
            if t.is_alive():
                t.join(timeout=0.5)

        print("[INFO 151] Servidor cerrado correctamente.")


# ---------------------------------------------------------
if __name__ == "__main__":
    # cargar conexion.json si existe
    try:
        with open("conexion.json", "r", encoding="utf-8") as f:
            cfg = json.load(f)
            host = cfg.get("host", HOST)
            port = int(cfg.get("port", PORT))
    except Exception:
        host, port = HOST, PORT

    server = Server(host=host, port=port)
    server.start()
