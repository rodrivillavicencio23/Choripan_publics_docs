champions = [["Real Madrid",15],["Juventus",2],["Inter de Milán",3],["Estrella roja de Belgrado",1],["Ajax",4]]

champions.sort(key=lambda x: x[1], reverse=False)
print(champions)

class Equipo:
    def __init__(self, nombre, champions_ganadas):
        self.nombre = nombre
        self.champions_ganadas = champions_ganadas
    
    def __str__(self):
        return f"El {self.nombre} tiene {self.champions_ganadas} Champions League en sus palmarés"


def trofeos(jugador):
    return jugador.champions_ganadas


equipo1 = Equipo('Bayern', 6)
equipo2 = Equipo('Varca Negreiralona', 5)
equipo3 = Equipo('AC Milán', 7)
equipo4 = Equipo("Man United",3)

print(equipo1)
print("")
jugadores = [equipo1, equipo2, equipo3, equipo4]
jugadores.sort(key=trofeos , reverse=True)
for i in jugadores:
    print(i)
