import threading
import time


def contar_hasta(num: int):
    for a in range (num):
        print(a)
        time.sleep(0.5)


hilo = threading.Thread(target=contar_hasta(num=20))
hilo_2 = threading.Thread(target=contar_hasta(num=30))
hilo.start()
hilo_2.join()

