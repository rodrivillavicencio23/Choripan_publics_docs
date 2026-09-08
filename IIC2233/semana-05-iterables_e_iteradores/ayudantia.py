
from typing import Any

class Tren():
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None
    
    def agregar(self, contenido, tipo):
        temp = Vagon(contenido, tipo)
        temp.colocar_siguiente(self.cabeza)
        self.cabeza = temp

    def cantidad(self):
        actual = self.cabeza
        contador = 0
        while actual is not None:
            contador += 1
            actual = actual.traer_siguiente()
        return contador

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.ver_dato(), end=" -> ")
            actual = actual.traer_siguiente()
        print("None")


class Vagon():
    def __init__(self, contenido: Any, tipo: Any):
        self.contenido = contenido
        self.tipo = tipo
        self.siguiente = None

    def ver_dato(self):
        return f"Tipo: {self.tipo} | Contenido: {self.contenido}"
    
    def traer_siguiente(self):
        return self.siguiente
    
    def entrar_dato(self, dato_nuevo, tipo_nuevo):
        self.contenido = dato_nuevo
        self.tipo = tipo_nuevo

    def colocar_siguiente(self, sig_nuevo):
        self.siguiente = sig_nuevo


# Uso:
tren = Tren()

tren.agregar("Carbon", "Vagón")
tren.agregar("Bananas", "Vagón")
tren.agregar("Combustible", "Vagón")
tren.agregar("Carbon", "Locomotora")



print("Contenido del tren:")
tren.mostrar()
