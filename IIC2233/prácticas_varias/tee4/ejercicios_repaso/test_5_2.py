import threading
import time


class Misil(threading.Thread):
    
    def __init__(self, nombre: str, tiempo_impacto: int, evento) -> None:
        super().__init__(name=nombre)
        self.tiempo_impacto = tiempo_impacto
        self.evento = evento

    def run(self):
        evento.wait()
        for a in range(self.tiempo_impacto, 0, -1):
            print(f"[{self.name}] impactando en {a} seg . . . ")
            time.sleep(0.25)
        print(f"{self.name} ha impactado !!")


evento = threading.Event()


misil_1 = Misil("Misil Balístico", 14, evento)
misil_2 = Misil("Misil de Crucero", 5, evento)


misil_1.start()
misil_2.start()


print("esperando . . . ")
time.sleep(3)
evento.set()

