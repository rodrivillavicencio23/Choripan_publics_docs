# ---------------------------------------------------------
# ---- Imports y modularización ----
import os
# ---------------------------------------------------------

# Limpiar terminal
def limpiar_cls():
    os.system("cls" if os.name == "nt" else "clear")

# Verificar que opción es válida
def validar_opcion(minimo: int, maximo: int) -> int:
    print(f"Indique su opción ({minimo}-{maximo}):")
    ingreso = input("------ ")
    if not ingreso.isdigit():
        return -1
    numero = int(ingreso)
    if numero < minimo or numero > maximo:
        return -1
    return numero