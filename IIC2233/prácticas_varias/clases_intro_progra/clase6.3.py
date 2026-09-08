from random import *

dado = randint(0,7)
seguir = True
intentos = 1
while seguir:
    player = int(input("Ingrese el n° de dado: "))
    if player == dado:
        print("GG ez adivinaste con", intentos, "intentos")
        seguir = False
    else:
        print("Sos malísimo perdisteeee")
        intentos +=1

while seguir == False:
    dado = randint(1,6)
    print(dado)
