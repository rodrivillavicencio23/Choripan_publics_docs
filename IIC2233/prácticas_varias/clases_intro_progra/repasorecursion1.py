"""def factorial(n):
    producto=1
    for i in range(1,n+1):
        producto*=i
    return producto

print(factorial(6))"""


"""def factorial2(n):
    if n==0:
        return 1
    return n*factorial2(n-1)

print(factorial2(5))"""


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)