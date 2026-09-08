aliados = [2, 5, 5, 1]
enemigos = [6, 2, 2]


print(aliados)
print(enemigos)

i = 0
while len(aliados) > 0 and len(enemigos):
    if enemigos[i] >= aliados[i]:
        enemigos[i]-=1
        aliados.pop(i)
        print("Zurg ha ganado esta ronda!")
    else:
        aliados[i] -=1
        enemigos.pop(i)
        print("buzz ha ganado esta ronda")

    print(aliados)
    print(enemigos)
    

if len(aliados) == 0:
    print("El malvado emperador Zurg tomara control de la Unimente!")
elif len(enemigos) ==0:
    print("Buzz! Nos has salvado, estamos agradecidos!")

