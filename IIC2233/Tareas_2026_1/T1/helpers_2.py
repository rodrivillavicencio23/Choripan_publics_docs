# -----------------------------------------------------------------------------
# Imports y modularización
from pathlib import os, Path
from random import random, randint
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Verificar que opción ingresada es válida
def validar_opcion(minimo: int, maximo: int) -> int:
    # solo existe una opción (min y max son iguales)
    if minimo >= maximo:
        print(f"Indique su opción ({minimo}):")
    else:
        print(f"Indique su opción ({minimo:^3d} - {maximo:^2d}):")
    ingreso = input("\n>>>>>>>")
    # Si no es un dígito/número
    if not ingreso.isdigit():
        return -1
    numero = int(ingreso)
    # Si el numero no está en el rango
    if numero < minimo or numero > maximo:
        return -1
    # número valido ...
    return numero

# -----------------------------------------------------------------------------
def validar_input():
    ingreso = input("\n>>>>>>>>")
    if ingreso == "":
        return False, "invalid_input"
    return True, ingreso

# -----------------------------------------------------------------------------
def validar_nombre_archivo():
    ingreso = input("\n>>>>>>>")
    # <>:"/\\|?*
    caracteres_prohibidos = [" ", "/", ".", "r\n", "<", ">", "\"", \
                             "!", "?", "#", "¡", "¿", "%", "&", ":", ";"]
    # prefijos prohibidos de inicio
    if ingreso.startswith(tuple(caracteres_prohibidos)):
        return "invalid_name" 
    # eliminar puntos
    lista_ingreso = list(ingreso)
    ingreso_sin_caracp = (b for b in lista_ingreso if b not in caracteres_prohibidos)
    ingreso_valido = "".join(ingreso_sin_caracp)
    print("\n-----------------------------\n")[:14]
    print("se ha limpiado el nombre en caso de existir caractéres no válidos \n \
          y se ha limitado a 15 caractéres")
    print("\n-----------------------------\n")
    return ingreso_valido

# -----------------------------------------------------------------------------
def validar_en_data(nombre_archivo:str) -> True|False:
    """ 
    Valida la existencia de un archivo en data (.csv),
    especificar que sea el nombre de archivo sin extensión
    """
    extendido = f"{nombre_archivo}.csv"
    ruta_a_data = os.path.join("data", extendido)
    if os.path.isfile(ruta_a_data):
        return True
    return False

# -----------------------------------------------------------------------------
def tirar_dados():
    """
    Retorna 2 valores en uno de dados aleatorios (1-6)
    """
    a = randint(1, 6)
    b = randint(1, 6)
    return a, b

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------