#Evaluar un puro número primo

n = int(input("Ingrese su número: "))

def primo_ono (n):
    a = 0
    siono = True
    for i in range (1, n+1):
        if n % i == 0:
            a+=1
    #Es primo
    if a == 2:
        print(f"{n} SÍ es primo")
        siono = True
    #No es primo
    elif a > 2:
        print(f"{n} NO es primo")
        siono = False
    return siono

choripan = primo_ono(n)
print(choripan)
