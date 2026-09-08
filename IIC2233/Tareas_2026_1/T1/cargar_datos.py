## ----------------------------------------------------------------------------
# carga_datos.py
# -----------------------------------------------------------------------------
# Imports y modularización
import os
from pathlib import Path
from personajes import Ayudante, Estudiante, Profesor, Sospechoso
from elementos import Arma, Habitacion
from helpers_2 import validar_en_data

# -----------------------------------------------------------------------------
def cargar_personajes():
    # Personajes
    list_personajes = []
    ruta_personajes = os.path.join("data", "personajes.csv")
    with open(ruta_personajes, "r") as lista_1:
        next(lista_1)
        for a in lista_1:
            b = a.rstrip('\n').split(",")
            tipo = b[1]
            nombre = b[0]

            if tipo == "Estudiante":
                personaje = Estudiante(nombre)
            elif tipo == "Ayudante":
                personaje = Ayudante(nombre)
            elif tipo == "Profesor":
                personaje = Profesor(nombre)
            else:
                continue
            list_personajes.append(personaje)
    return list_personajes

# -----------------------------------------------------------------------------
def cargar_habitaciones():
    # Habitaciones
    list_habitaciones = []
    ruta_habitaciones = os.path.join("data", "habitaciones.csv")
    with open(ruta_habitaciones, "r") as lista_2:
        next(lista_2)
        for a in lista_2:
            b = a.rstrip('\n').split(",")
            habitacion = Habitacion(b[0], b[1], b[2])
            list_habitaciones.append(habitacion)
    return list_habitaciones

# -----------------------------------------------------------------------------
def cargar_armas():
    # Armas
    list_armas = []
    ruta_armas = os.path.join("data", "armas.csv")
    with open(ruta_armas, "r") as lista_3:
        next(lista_3)
        for a in lista_3:
            b = a.rstrip('\n').split(",")
            arma = Arma(b[0], b[1])
            list_armas.append(arma)
    return list_armas

# -----------------------------------------------------------------------------
def crear_pistas_csv(lista_pistas: list[Sospechoso]):

    ruta = os.path.join("data", "pistas.csv")
    with open(ruta, "w", encoding="UTF-8") as archivo_csv:
        archivo_csv.write("nombre_personaje,tipo_personaje,pista_personaje,pista_arma,pista_sala")
        for line in lista_pistas:
            archivo_csv.write(f"{line.nombre},{line.tipo},{line.pistas}")

# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------

