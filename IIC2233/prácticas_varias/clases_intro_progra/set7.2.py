a = int(input())
lista1 = []
ordenado = []
for b in range(a):
    c = input()
    d = c.split(" ")
    d[1]= d[1].split(",")
    efe =""
    for e in d[1]:
        efe+=e
    d[1]= efe
    d[0]= int(d[0])
    lista1.append(d)

print(lista1)