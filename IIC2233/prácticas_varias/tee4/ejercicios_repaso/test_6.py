import threading
import time
import os
from random import random
import typing


class EscritorArchivo(threading.Thread):
    """
    Esta clase modela un thread. Dentro creamos un objeto para bloqueo dentro de la clase. 
    El Lock es una variable independiente de cada thread y es común para todas las instancias.
    """

    # Atributo de clase
    # Accesible mediante Clase.lock o self.lock desde una instancia
    lock = threading.Lock()

    def __init__(self, numero: int, archivo: typing.TextIO) -> None:
        # Mandamos un nombre a la clase padre con el atributo name
        super().__init__(name=f"EscritorArchivo número {numero}")
        self.numero = numero
        self.archivo = archivo

    def run(self) -> None:
        print(f"[{self.name}] ¡Comenzó a trabajar!")
        for _ in range(self.numero):
            with self.lock:  # Acceso al lock
                self.archivo.write(f"Línea escrita por # {self.name}\n")
                print(f"[{self.name}] ¡escribió una línea!")
            # Hacemos que se demore una cantidad random uniforme [0, 1)
            time.sleep(random())


# Creamos un archivo para escribir una salida
# Luego creamos los threads que escribirán dentro del archivo
with open(os.path.join("files", "salida.txt"), "w", encoding="utf-8") as archivo:
    # Creamos los threads
    cantidad_threads = 8

    threads = []
    for i in range(1, cantidad_threads + 1):
        threads.append(EscritorArchivo(i, archivo))

    # Hacemos partir los threads
    for thread in threads:
        thread.start()

    # Esperamos a todos los threads antes de cerrar el archivo
    for thread in threads:
        thread.join()

    print("Todos los threads terminaron. Revise el resultado en files/salida.txt")