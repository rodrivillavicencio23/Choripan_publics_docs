def factorial(number):
    if number > 1:
        number = number * factorial(number -1)
    return number

a = int(input())
print(factorial(a))


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)