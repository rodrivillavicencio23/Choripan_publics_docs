from typing import Any

class Lista():
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None
    
    def agregar(self, dato):
        temp = Vagon(dato)
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
    def __init__(self, contenido: Any):
        self.contenido = contenido
        self.siguiente = None

    def ver_dato(self):
        return self.contenido
    
    def traer_siguiente(self):
        return self.siguiente
    
    def entrar_dato(self, DatoNuevo):
        self.contenido = DatoNuevo

    def colocar_siguiente(self, sigNuevo):
        self.siguiente = sigNuevo


# Uso:
tren = Lista()
tren.agregar("plata")
tren.agregar("carbon")
tren.agregar("bananas")

print("Contenido del tren:")
tren.mostrar()
