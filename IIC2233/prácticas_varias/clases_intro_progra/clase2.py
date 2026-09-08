from random import *

#Variables de la máquina
cachipun = ["Piedra","Papel", "Tijera"]
machine = randint(0,2)
print(machine)
option = cachipun[machine]

#Variable del usuario
user = int(input("elige tu mano pibe: 0-Piedra, 1-Papel , 2-Tijera: "))
print(user)
print("el usuario eligió: ",cachipun[user])
#comprobación de variables
print("la máquina eligió: ",option)

#Condicional de victoria, derrota o empate

#Papel y Tijera
if machine == 1 and user == 2:
    print("Ganaste GG EZ")
elif machine == 2 and user == 1:
    print("Perdiste Pibe no tenes niun brillo")

#Piedra y Papel
elif machine ==0  and user == 1:
    print("Ganaste GG EZ")
elif machine ==1  and user == 0:
    print("Perdiste Pibe no tenes niun brillo")

#Piedra y Tijera
elif machine == 2 and user == 0:
    print("Ganaste GG EZ")
elif machine == 0 and user == 2:
    print("Perdiste Pibe no tenes niun brillo")

#Empate para cualquier caso
elif machine == user:
    print("empate")


