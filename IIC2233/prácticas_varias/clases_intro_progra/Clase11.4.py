#Clase11.4
#Evaluar rango de numeros primos

n = int(input("Ingrese su rango de números: "))

def primos_ono (n):
    
    for number in range(1,n+1):
        a = 0
        siono = True
        for divi in range(1,number+1):
            if number % divi == 0:
                a+=1
        #Es primo
        if a == 2:
            print(f"{number} SÍ es primo")
            siono = True
        #No es primo
        elif a > 2:
            print(f"{number} NO es primo")
            siono = False
    return siono

primos_ono(n)



    