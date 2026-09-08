# cliente/test_client.py
import socket
import sys
import time
import json

HOST = "127.0.0.1"
PORT = 15100

def run():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    # espera handshake
    data = s.recv(1024).decode()
    print("Server:", data.strip())
    # enviar nombre de usuario
    name = input("Nombre de usuario de prueba: ").strip()
    s.sendall(name.encode())
    resp = s.recv(1024).decode()
    print("Server:", resp.strip())
    # enviar mensajes de prueba
    while True:
        msg = input("-> ")
        if msg.lower() in ("exit", "quit"):
            s.sendall(msg.encode())
            break
        s.sendall(msg.encode())
        echo = s.recv(4096).decode()
        print("Server:", echo.strip())
    s.close()

if __name__ == "__main__":
    run()
