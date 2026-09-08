# ------------------------------
# Imports y Modularización
import socket
import json
import time
from pathlib import Path

# ------------------------------

ENCODING = "UTF-8"
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 15100
RECV_SIZE = 4096
RETRY_DELAY = 1.0
MAX_RETRIES = 3
SOCKET_TIMEOUT = 5

def load_connection_config():
    try:
        from server.parametros import HOST as P_HOST, PORT as P_PORT
        return str(P_HOST), int(P_PORT)
    except Exception:
        pass

    for path in ("conexion.json", "server/conexion.json", "client/../server/conexion.json"):
        p = Path(path)
        if p.exists():
            try:
                data = json.loads(p.read_text(encoding="utf-8"))
                return data.get("host", DEFAULT_HOST), int(data.get("port", DEFAULT_PORT))
            except FileNotFoundError:
                pass

    return DEFAULT_HOST, DEFAULT_PORT

# ------------------------------
class ConnectionHandler:
    def __init__(self, host=None, port=None):
        if host is None or port is None:
            host, port = load_connection_config()
        self.host = host
        self.port = int(port)
        self.sock = None

    def connect(self, retries=MAX_RETRIES):
        last_exc = None
        for attempt in range(1, retries + 1):
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.settimeout(SOCKET_TIMEOUT)
                self.sock.connect((self.host, self.port))
                self.sock.settimeout(None)
                return True
            except ValueError as e:
                last_exc = e
                print(f"[WARN] Intento {attempt} fallo: {e}. Reintentando en {RETRY_DELAY}s...")
                try:
                    self.sock.close()
                except OSError:
                    pass
                time.sleep(RETRY_DELAY)
        print(f"[ERROR] No se pudo conectar a {self.host}:{self.port} - {last_exc}")
        return False

    def close(self):
        try:
            if self.sock:
                self.sock.shutdown(socket.SHUT_RDWR)
                self.sock.close()
        except Exception:
            pass
        finally:
            self.sock = None

    def send_text(self, text: str):
        if not self.sock:
            raise RuntimeError("Socket no conectado")
        self.sock.sendall(text.encode(ENCODING))

    def recv_text(self, size=RECV_SIZE) -> str:
        if not self.sock:
            raise RuntimeError("Socket no conectado")
        data = self.sock.recv(size)
        if not data:
            return ""
        return data.decode(ENCODING)

    def handshake_and_auth(self, username: str) -> bool:

        if not self.sock:
            raise RuntimeError("Socket no conectado")

        # 1. recibir banner
        banner = self.recv_text(1024).strip()
        print("[SERVER]", banner)

        if banner != "HANDSHAKE NOMBRE":
            print("[ERROR] Protocolo inesperado:", banner)
            return False

        # 2. enviar username
        self.send_text(f"USERNAME {username}")

        # 3. recibir respuesta
        resp = self.recv_text(1024).strip()
        print("[SERVER]", resp)

        if resp.startswith("WELCOME"):
            return True

        if resp.startswith("ERROR"):
            print("[ERROR] Nombre en uso")
            return False

        print("[ERROR] Respuesta inesperada:", resp)
        return False