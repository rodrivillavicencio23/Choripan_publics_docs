import socket
import threading

class Server:
    def __init__(self, host='localhost', port=15100):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        self.active_users = set()  # Para almacenar nombres de usuario activos
        print(f"Servidor escuchando en {self.host}:{self.port}")

    def handle_client(self, conn, addr):
        print(f"Cliente conectado desde {addr}")

        # Validación de nombre de usuario
        while True:
            conn.sendall("Ingrese su nombre de usuario: ".encode('utf-8'))
            username = conn.recv(1024).decode('utf-8').strip()
            if username and username not in self.active_users:
                self.active_users.add(username)
                conn.sendall(f"Bienvenido {username}, puedes empezar a enviar mensajes.\n".encode('utf-8'))
                print(f"Usuario '{username}' conectado desde {addr}")
                break
            else:
                conn.sendall("Nombre inválido o ya en uso. Intente otro.\n".encode('utf-8'))

        # Recepción de mensajes
        while True:
            data = conn.recv(1024).decode('utf-8')
            if not data or data.lower() == 'exit':
                break
            print(f"[{username}] dice: {data}")

        # Al cerrar conexión, eliminar usuario
        self.active_users.remove(username)
        conn.close()
        print(f"Usuario '{username}' desconectado")

    def start(self):
        while True:
            conn, addr = self.server_socket.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f"Hilo iniciado para cliente {addr}")

if __name__ == "__main__":
    server = Server()
    server.start()