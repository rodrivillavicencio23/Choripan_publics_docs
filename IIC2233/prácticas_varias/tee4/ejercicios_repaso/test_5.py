import threading
import time

lock = threading.Lock()

def disparar_misil(tiempo_impacto: int):
    thread_actual = threading.current_thread()
    
    print("Lanzando Misil")
    for a in range(tiempo_impacto, 0, -1):
        print(f"{a}...")
        time.sleep(0.5)
    print(f"{thread_actual.name} ha impactado a las {time.strftime("%H:%M:%S")}!")

hilo_1 = threading.Thread(name="MISIL 1", target=disparar_misil, args=(10,))
hilo_2 = threading.Thread(name="MISIL 2", target=disparar_misil, args=(4,))


hilo_1.start()
hilo_1.join(timeout=2)
hilo_2.start()
