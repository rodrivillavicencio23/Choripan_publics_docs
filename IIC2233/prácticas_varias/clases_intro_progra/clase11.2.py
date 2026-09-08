#clase 11.2

n = int(input("ingrese número factorial: "))

def factorial (n):
    multi = 1
    if n == 0:
        multi = 1
        return multi
    elif n < 0:
        multi = 0
        return multi
    else:
        for a in range (1,n+1):
            multi *= a
        n = 0
        return multi

y = (factorial(n))
print(f"{n}! = {y}")
