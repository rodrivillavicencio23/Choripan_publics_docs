# ---------------------------------------------------------
# ---- Imports y modularización ----
import sys
from jugador import Jugador
from dccatastrofe import leer_ia
from menus import menu_principal
from functions import limpiar_cls
from arts import corazon_dcc
# ---------------------------------------------------------

def main():
    args = sys.argv
    dificultad = args[1] if len(args) > 1 else "facil"

    limpiar_cls()
    corazon_dcc()

    nombre = input("Ingrese nombre de usuario: ").strip()
    if not nombre:
        nombre = "Usuario_1"
        print("Se asignó nombre predeterminado.")

    jugador = Jugador(nombre)
    ia_actual = leer_ia(dificultad)

    menu_principal(jugador, ia_actual)

if __name__ == "__main__":
    main()
