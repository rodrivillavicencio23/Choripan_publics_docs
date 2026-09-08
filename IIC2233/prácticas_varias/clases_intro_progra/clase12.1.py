#Strings
#Clase 12
mayor = 0
seguir = True
n= 0
while seguir:
    n = int(input())
    if n == -1:
        seguir = False
    elif n > mayor:
        mayor = n
print(f"el número mayor es {mayor}")
