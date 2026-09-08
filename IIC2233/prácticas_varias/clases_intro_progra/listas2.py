reloj = [0,0]


while reloj[1] < 61 and reloj[0] != 24:
    reloj[1]+=1
    if reloj [1] == 60:
        reloj[0]+=1
        reloj[1] = 0


    print(reloj)

print(reloj)

