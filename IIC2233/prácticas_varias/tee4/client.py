import socket



class Client:
    def __init__(self, host='localhost', port=15100):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client_socket.connect((self.host, self.port))
        print(f"Conectado al servidor en {self.host}:{self.port}")

    def chat(self):
        while True:
            server_msg = self.client_socket.recv(1024).decode('utf-8')
            print(server_msg, end="")  # Mostrar mensaje del servidor
            if "Bienvenido" in server_msg:
                break
            username = input("> ")
            self.client_socket.sendall(username.encode('utf-8'))

        print("Escribe mensajes para enviar al servidor. Escribe 'exit' para salir.")
        while True:
            message = input("> ")
            self.client_socket.sendall(message.encode('utf-8'))
            if message.lower() == 'exit':
                break

        self.client_socket.close()
        print("Conexión cerrada.")

if __name__ == "__main__":
    client = Client()
    client.connect()
    client.chat()