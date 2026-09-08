def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1)*n

print(factorial(5))

def fibonacci(xd):
    print("xd")


def largo(lista):
    if lista == []:
        return 0
    
    return largo(lista[1:])+1