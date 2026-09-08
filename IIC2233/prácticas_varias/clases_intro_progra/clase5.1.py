n = 1
qn = int(input("ingrese cantida de notas: "))
b=0
while n<=qn:
    p=float(input("ingrese nota: "))
    b=b+p
    n+=1
promedio = float(b / qn)
print(promedio)
