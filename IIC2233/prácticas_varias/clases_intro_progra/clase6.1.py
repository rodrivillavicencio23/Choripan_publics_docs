#Variables
sum = 0
notes = int(input("Ingrese cantidad de notas:"))
n = notes
follow = True
#Promediar notas
while follow:
    note = float(input("Ingrese nota: "))
    sum+=note
    n-=1
    if n == 0:
        follow = False
        print("Las notas promediadas dan: ",(sum/notes))
    
#break: solo dentro de if (o elif, o else), deja de ejecutar el ciclo
#inmediatamente y continúa con instrucciones después