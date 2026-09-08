from random import *

#Variables

usern = int(input("intenta adivinar el número del dado: "))
print("el usuario escogió el número: ", usern)
dado = randint(1,6)
print("La máquina eligió: ",dado)

#Función Condicional
def comprobardado ():
    if usern == dado:
        print("haz acertado")
    else:
        print("haz perdido bot")
    return
comprobardado()


print("----------------------------------------------------------------------------------")
#Apunte
#Apunte
xd=random()*100
print(xd)
x=100
x+=1

print(x)