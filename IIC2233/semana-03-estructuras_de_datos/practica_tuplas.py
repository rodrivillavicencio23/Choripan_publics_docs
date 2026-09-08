from typing import Tuple, NamedTuple
from collections import namedtuple
import os
import time

un_verano_sin_ti: tuple = (
                    "Después de la playa",
                    "Otro Atardecer", 
                    "Un ratito", 
                    "La Corriente", 
                    "Party", 
                    "Andrea")



#'''
try:
    un_verano_sin_ti[1] = "Moscow Mule"
except TypeError:
    print("No se puede hacer eso brother")

#'''

print(type(un_verano_sin_ti), f"| elemento 1: {un_verano_sin_ti[0]}")


# ------------------------------------
# Desempaquetado de tuplas:
# ------------------------------------
cancion_uvst = ("Party", "Bad Bunny y Rauw Alejandro", 2022, "party.txt")


def reproducir_cancion(cancion: str, artistas: str, año: int, ruta: str):
    print(f"\t -----------------\n" \
    f"\t {cancion} \n"
    f"\t {artistas} \n"
    f"\t {año} \n"
    "\t ----------------")
    nueva_ruta = os.path.join("songs", ruta)
    with open(nueva_ruta, "r", encoding="UTF-8") as letras:
        for linea in letras:
            linea_m = linea.rstrip()
            print(linea_m)
    return
    
reproducir_cancion(*cancion_uvst)

print("-------------------")


# ------------------------------------
# Slicing
# ------------------------------------

print(un_verano_sin_ti[:3])
print(un_verano_sin_ti[::-1])

# ------------------------------------
# Named Tuples
# ------------------------------------

CancionX100pre = namedtuple("Cancion_X100pre",["nombre_cancion","artistas","fecha", "año", "millones_views"])

mejor_cancion = CancionX100pre("NI BIEN NI MAL","Bad Bunny", "01012020", 2020, 223)

print(mejor_cancion.año)

# ver el tipo de objeto (por eso se define un nombre antes de la lista)

print(mejor_cancion.__class__)

