#Listas de listas

lista = ["xd","choripan",[1,2,3]]

print(lista[2][0])
print(lista[1][0:5])

bayern = [33,45,115]

def agregarenlista (bayern,xd):
    bayern.append(xd)
    bayern.sort()
    return bayern


cabrontunove = int(input("ingresa número: "))
colocolo = agregarenlista(bayern,cabrontunove)
print(colocolo)