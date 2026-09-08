import threading

import time
import sys

def contar_diez_segundos() -> None:
    print("Iniciando contador del TheGreg...")
    for numero in range(1, 11):
        # print(f"({numero} segundo{'s' if numero > 1 else ''})")
        time.sleep(1)

    print("Cobra mercenario moriste en Madrid 9/12...")
    return 0

mi_hilo = threading.Thread(target=contar_diez_segundos, daemon=True)




mi_hilo.start()

list_1 = []
while mi_hilo.is_alive():
    oye = input()
    list_1.append(oye)
    if oye == "1":
        sys.exit()


print(list_1)