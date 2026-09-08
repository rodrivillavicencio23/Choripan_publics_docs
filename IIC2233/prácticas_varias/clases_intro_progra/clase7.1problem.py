from random import *
puntos1 = 0
puntos2 = 0
turno1 = 0
turno2 = 0

jugador1 = str(input("Ingrese nombre jugador 1: "))
jugador2=str(input("Ingrese nombre jugador 2: "))
while puntos1 < 30 and puntos2 <30:
    turno = int(input("1. Juega jugador 1 | 2. Juega jugador2"))
    if turno == 1:
        turno2 = 0
        #Jugador 1
        dado1 = randint(1,6)
        print("turno de",jugador1,":")
        print("dado 1 n°: ",dado1, "| Puntos actuales:",puntos1)
        
        if dado1 == 1:
            print("perdiste tus últimos puntos", puntos1,"XDDD")
            puntos1-= turno1
        else:
            puntos1 += dado1
            turno1 += dado1
    elif turno == 2:
        turno1 = 0
        #Jugador 2
        dado2 = randint(1,6)
        print("turno de",jugador2,":")
        print("dado 2 n°: ",dado2, "| Puntos actuales:",puntos2)
        if dado2 == 1:
            print("perdiste tus últimos puntos",jugador2,"JAJAJ")
            puntos2-= turno2
        else:
            puntos2 +=dado2
            turno2 += dado2

if puntos1 >= 30:
    print(jugador1, "es el Ganador con: ",puntos1,"puntos")
elif puntos2 >=30:
    print(jugador2,"es el Ganador con: ",puntos2,"puntos")