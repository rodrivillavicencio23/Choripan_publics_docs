#Funciones clase 11
hora = 141520
def segundos (hora):
    s = hora%100
    m = (hora//100)%100
    h = (hora//10000)%100
    return s*+m*60+h*60*60


n = int(input("ingrese número factorial"))

def factorial (n):
    multi = 1
    for a in range (1,n+1):
        multi *= a
    n = 0
    return multi

y = (factorial(n))
print(f"{n}! = {y}")

