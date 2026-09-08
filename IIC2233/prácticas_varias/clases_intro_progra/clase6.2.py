#Variables
caja_notas = []
sum = 0
notes = int(input("Ingrese cantidad de notas:"))
n = notes
follow = True

while follow:
    note = float(input("Ingrese nota: "))
    caja_notas.append(note)
    n-=1
    if n == 0:
        follow = False
print("la nota más alta es: ",max(caja_notas))