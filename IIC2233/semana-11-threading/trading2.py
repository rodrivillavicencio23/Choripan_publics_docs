import threading

def saludar() -> None:
    thread_actual = threading.current_thread()
    print(f"Hola desde {thread_actual.name}\n")


hilo_1 = threading.Thread(name="Mi thread 1 chingón", target=saludar)
hilo_2 = threading.Thread(name="Mi thread 2 parce", target=saludar)


# Llamaremos a saludar() desde los threads nombrados
hilo_1.start()
hilo_2.start()
# Ahora llamaremos a saludar() desde el thread principal
saludar()