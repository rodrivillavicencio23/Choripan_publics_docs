# Esto es para el ejemplo de 2 MODULARIZACIÓN

PI = 3.14159

def saludar(nombre):
    return f"Hola, {nombre}!"

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return PI * (self.radio ** 2)