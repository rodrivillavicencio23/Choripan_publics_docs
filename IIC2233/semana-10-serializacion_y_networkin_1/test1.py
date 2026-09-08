from os import path
import pathlib
import requests
import json


lista = ["a", 1, "choripan", "hola"]
lista_serializada = json.dumps(lista)


print(lista_serializada)


with open(path.join("mi_lista.json"), "w") as archivo:
    json.dump(lista, archivo)

