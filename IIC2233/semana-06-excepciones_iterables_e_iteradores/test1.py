def test(x):
    try:
        r = 10 / x
    except ZeroDivisionError:
        print("A")
        return -1
    else:
        print("B")
        return r
    finally:
        print("C")

print(test(2))
print("---")
print(test(0))