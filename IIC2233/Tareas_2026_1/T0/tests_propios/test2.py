""" 
Comentario grande:

Sea "equisde" un archivo y .txt su extensión, el
cual está alojado en carpeta "dir",
contenido del archivo <equisde.txt>:
bocashoteamo
hola
pe
causa

"""
from pathlib import os
# o también puedes importar
import os

nombre_archivo = "equisde"
archivo_mas_extension = f"{nombre_archivo}.txt" #f string
ruta_completa = os.path.join("dir", archivo_mas_extension)

info = [] # lista donde guardaremos la info
with open(ruta_completa, "r", encoding="UTF-8") as nombre_lista_archivo: 
    # encoding utf-8 para reconocer caracteres como la Ñ
    primera_linea = nombre_lista_archivo.readline() # bocashoteamo (casi como un salto de linea)
    for linea in nombre_lista_archivo:
        nueva_linea = linea.rstrip("\n")
        lista_nueva_linea = list(nueva_linea) # ["h", "o", "l", "a"]
        info.append(lista_nueva_linea)

# con el with open no tienes que asegurarte de cerrar el archivo
# ya lo hace por su cuenta al terminar sus líneas
print(primera_linea)
print(info)
""" 
output esperado (estado lista info):

bocashoteamo

["h", "o", "l", "a"]
["p", "e"]
["c", "a", "u", "s", "a"]

"""


