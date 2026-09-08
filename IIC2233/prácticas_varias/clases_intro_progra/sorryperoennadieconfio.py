def factores_primos(n):
    b  = 0
    for a in range(2,int(n)):
        if n % a == 0:
            print(a)
            return factores_primos(n//a)
        elif n == 1:
            return
    print(int(n))
    return

print(factores_primos(1156))