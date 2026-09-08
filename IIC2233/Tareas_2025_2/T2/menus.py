# ---------------------------------------------------------
# ---- Imports y modularización ----
from functions import validar_opcion, limpiar_cls
from arts import troll_face_2, fraudales
# ---------------------------------------------------------

def mostrar_header(usuario: str):
    """Muestra encabezado de juego."""
    print("|----------------------------------------------------|")
    print("¡Bienvenido a DCCartas!")
    print("|----------------------------------------------------|")
    print(f"Usuario: {usuario if usuario else 'Usuario_1'}")


# ---------------------------------------------------------
# Menú Principal
def menu_principal(jugador, ia_actual):
    """Menú principal del juego."""
    while True:
        print("-----------------------------")
        print("MENÚ PRINCIPAL\n")
        print(f"Usuario: {jugador.nombre}")
        print("-----------------------------\n")
        print(f"Dinero disponible: {jugador.oro} G")
        print("Ronda Actual: 1")
        print(f"IA enemiga: {ia_actual.nombre} (Vida {ia_actual.vida})\n")
        print("-----------------------------")
        print("[1] Entrar en combate")
        print("[2] Inventario (gestionar mazo)")
        print("[3] Tienda")
        print("[4] Ver información de mis cartas")
        print("[5] Espiar a la IA")
        print("[6] Salir del juego")

        opcion = validar_opcion(1, 6)
        if opcion == -1:
            limpiar_cls()
            print("Ingrese un valor válido dentro de los entregados ;D")
            troll_face_2()
            continue

        match opcion:
            case 1:
                print("Combate en progreso... (TODO)")
            case 2:
                print("Inventario en progreso... (TODO)")
            case 3:
                menu_tienda(jugador)
            case 4:
                print("Mostrar cartas en progreso... (TODO)")
            case 5:
                print(f"Erespiando a {ia_actual.nombre}... (TODO)")
            case 6:
                print("Cerrando juego, gracias por jugar! :3")
                fraudales()
                break


# ---------------------------------------------------------
# Menú Tienda
def menu_tienda(jugador):
    """Menú de la tienda, permite comprar y acceder al taller."""
    while True:
        print("-----------------------------")
        print("TIENDA")
        print("-----------------------------")
        print(f"Dinero disponible: {jugador.oro} G\n")
        print("Cartas disponibles:")
        print("[1] Duende .......... 5G")
        print("[2] Montapatos ...... 10G")
        print("[3] Cañón ........... 12G")
        print("[4] Caballero ....... 15G")
        print("---- Opciones ----")
        print("[6] Curar carta")
        print("[7] Revivir carta del cementerio")
        print("[8] Reroll catálogo (costo 3G)")
        print("[9] Taller (combinar cartas)")
        print("[0] Volver al Menú principal")

        opcion = validar_opcion(0, 9)
        if opcion == -1:
            limpiar_cls()
            print("Ingrese un valor válido dentro de los entregados ;D")
            troll_face_2()
            continue

        match opcion:
            case 1:
                print("Comprar Duende... (TODO)")
            case 2:
                print("Comprar Montapatos... (TODO)")
            case 3:
                print("Comprar Cañón... (TODO)")
            case 4:
                print("Comprar Caballero... (TODO)")
            case 6:
                print("Curar carta... (TODO)")
            case 7:
                print("Revivir carta... (TODO)")
            case 8:
                print("Reroll catálogo... (TODO)")
            case 9:
                menu_taller(jugador)
            case 0:
                break


# ---------------------------------------------------------
# Menú Taller
def menu_taller(jugador):
    """Menú del taller, permite combinar cartas."""
    while True:
        print("-----------------------------")
        print("TALLER")
        print("-----------------------------\n")
        print("Recetas disponibles:")
        print("[1] Montapatos + Cañón -> Montapatos-Cañón")
        print("[2] Caballero + Torre DIE -> Caballero-Torre DIE")
        print("[3] Volver a Tienda")

        opcion = validar_opcion(1, 3)
        if opcion == -1:
            limpiar_cls()
            print("Ingrese un valor válido dentro de los entregados ;D")
            troll_face_2()
            continue

        match opcion:
            case 1:
                print("Combinando Montapatos + Cañón... (TODO)")
            case 2:
                print("Combinando Caballero + Torre DIE... (TODO)")
            case 3:
                break