# -------------------
# --- Imports
import os
# -------------------

artistas = ["bad bunny", "Daddy Yankee", "Pablo Alboran", "Rauw Alejandro"]
print("\n -------------- ")
print([a for a in artistas])

largo_artistas = [len(artista) for artista in artistas]
print(largo_artistas)


# 1eros 3 caracteres
print("\n -------------- ")
lista_1 = [artista[:3] for artista in artistas]
print(lista_1)

# Separar a sublistas

sub_listas = [artista.split() for artista in artistas]
print(sub_listas)

arch = "IO_archivo_ejemplo_3"
file = os.path.join("data",arch)
with open(file, "r", encoding="UTF-8") as lineas_archivo:
    recuperar_lineas = [linea.rstrip().split(",") for linea in lineas_archivo if linea[1].endswith("1")]
print(recuperar_lineas)





"""
• a[start:end]: retorna los elementos desde start hasta end - 1.

• a[start:]: retorna los elementos desde start hasta el final del arreglo.

• a[:end]: retorna los elementos desde el principio hasta end - 1.

• a[:]: crea una copia (shallow) del arreglo completo. Es decir, el arreglo retornado 
está en una nueva dirección de memoria, pero los elementos que están en este 
nuevo arreglo, hacen referencia a la dirección de memoria de los elementos del 
arreglo inicial.

• a[start:end:step]: retorna los elementos desde start hasta no pasar end, en 
pasos de a step.
• a[-1]: retorna el último elemento en el arreglo.

• a[-n:]: retorna los últimos n elementos en el arreglo.

• a[:-n]: retorna todos los elementos del arreglo menos los últimos n elementos

"""