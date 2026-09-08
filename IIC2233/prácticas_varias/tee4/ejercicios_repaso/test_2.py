class Helicoptero:
    def __init__(self, nombre, potencia: int):
        self.nombre = nombre
        self._potencia = potencia


    @property #getter
    def potencia(self):
        # accediendo a potencia . . .
        return f"{self._potencia}.0 HP"
    def __str__(self):
        return f"{self.nombre} | {self.potencia}"
    

    @potencia.setter
    def potencia(self, nuevo_valor):
        if nuevo_valor < 0:
            print("¡Error! La potencia no puede ser negativa.")
        else:
            print(f"Cambiando potencia a {nuevo_valor}")
            self._potencia = nuevo_valor
    
    


heli_1 = Helicoptero("Mi-24NVM", 2225)

print(heli_1)

heli_1.potencia = 500

print(heli_1.potencia)