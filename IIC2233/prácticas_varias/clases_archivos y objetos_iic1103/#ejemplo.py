#ejemplo

class Jugador:
    def __init__(self,nombre,goles):
        self.nombre = nombre
        self.goles = goles

    def __str__(self):
        return (f"El jugador llamado {self.nombre} ha convertido {self.goles} goles en su carrera")
    
jugador1 = Jugador("Penaldo",937)

print(jugador1)
        