notas = []
seguir = True
while seguir:
    nota = int(input("Ingrese nota: "))
    if nota == -1:
        seguir = False
    else:
        notas.append(nota)

print(notas)
print("promedio: ",round((sum(notas)/len(notas)),2))