from queue import Queue
from random import choices
import threading
import time


piezas_de_pan = Queue()


def panadero() -> None:
    # El panadero hará 3 veces pan
    for partida in range(3):
        # En cada vez, producirá 5 piezas de pan.
        # Se demorará 5 segundos por vez (que rápido :D)
        time.sleep(5)
        print("[Panadero] Produje 5 piezas de pan en la partida", partida)
        piezas = choices(["Marraqueta", "Baguette", "Hallulla", "Queque"], k=5)
        for pieza in piezas:
            piezas_de_pan.put(pieza)


def cliente(i: int) -> None:
    print(f"[Cobra {i}] ¡Quiero Queque!")
    mi_pan = piezas_de_pan.get()
    print(f"[Cobra {i}] ¡Saqué mi {mi_pan}!")
    piezas_de_pan.task_done()


thread_panadero = threading.Thread(target=panadero)
threads_clientes = []

for i in range(15):
    threads_clientes.append(threading.Thread(target=cliente, args=(i, )))

thread_panadero.start()
for thread_cliente in threads_clientes:
    thread_cliente.start()

# Esperamos a que todos los threads finalicen para que esta celda termine con su ejecución
for thread_cliente in threads_clientes:
    thread_cliente.join()

