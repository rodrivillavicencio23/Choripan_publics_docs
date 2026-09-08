import os


def ordenar_lista(lista_sort):
    return lista_sort[0]
file = open('archivo.csv')
datos = file.readlines()
print(datos)

for a in datos:
    a.strip('\n')
    a.split(';')
    print(a)

