import threading
import time
import random

def misil(seg: int):
    for a in  range(seg, 0, -1):
        # thread_actual = threading.current_thread()
        print(f"Misil Impactando en {a} seg/s")
        time.sleep(0.2)

misil_1 = threading.Thread(target=misil, args=(10,), name="MISIL-2")
misil_2 = threading.Thread(target=misil, args=(15,), name="MISIL-2")
misil_1.start()
misil_2.start()
misil_1.join()
print("este mensaje se mostrará luego de que termine el misil")
misil_2.join()
print("y este mensaje??")


print("Disparo de misiles múltiples (estos van para Haifa)")
misiles = []
for a in range(4,7):
    misiles.append(threading.Timer(5, misil, args=(random.randint(4,8),)))

for misil in misiles:
    misil.start()