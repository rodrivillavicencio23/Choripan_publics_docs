votos = []
seguir = True

while seguir:
    voto = int(input())
    if voto == -1:
        seguir = False
    else:
        votos.append(voto)

print(votos)
unicos = []
for a in votos:
    if a not in unicos:
        unicos.append(a)
    else:
        pass

print(unicos)
mayor = 0
for a in unicos:
    m = votos.count(a)
    print(str(a),"--> votos: ",m)
    if m > mayor:
        mayor = a

print(f"ganador de la votación: {mayor}")