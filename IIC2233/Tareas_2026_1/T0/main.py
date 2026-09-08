# -------------------------------------------------------------------
# Imports y modularización
from pathlib import Path
from helpers import validar_opcion, validar_input, validar_en_data
from dccolores import DCColores
from visualizador import tablero_a_texto

# -------------------------------------------------------------------
# Menús de juego
# -------------------------------------------------------------------

# -------------------------------------------------------------------
# Menú principal
# -------------------------------------------------------------------
def main():

    iic2233 = DCColores()
    """ 
    Menú inicial del juego
    """

    # Si el jugador presiona Enter se asigna un nombre predeterminado
    nombre_jugador = input("Ingrese nombre de jugador. . .")
    if nombre_jugador == "":
        nombre_jugador = "Jugador_1"

    print("\n.\n.\n cargando ... \n.\n.\n")
    while True:
        print("\n-----------------------------")
        print("-----------------------------\n")
        print("\n MENÚ PRINCIPAL\n")
        print(f"Username: {nombre_jugador}\n")
        print("-----------------------------")
        print("[1] Abrir tablero")
        # enumerar opciones de entrada y de tableros que se vayan abriendo
        for num ,table in enumerate(iic2233.tableros, start=2):
            print(f"[{num}] {table}")

        print("[0] Salir del programa")
        print("-----------------------------")

        opcion = validar_opcion(0, len(iic2233.tableros)+1)
        if opcion == -1:
            print("\n-----------------------------\n")
            print("Ingrese un valor válido dentro de los dados :D")
            print("\n-----------------------------\n")
        else:
        
            match opcion:
                # Abrir tablero a partir de input del usuario
                case 1:
                    print("\n-----------------------------\n")
                    print("Ingrese el nombre del archivo sin la extensión de este:")
                    print("\n-----------------------------\n")

                    nombre_archivo_abrir = input(">>>>>>>>")
                    valido = validar_en_data(nombre_archivo_abrir)
                    if valido:
                        iic2233.cargar_tablero(nombre_archivo_abrir)
                        print("\n-----------------------------\n")
                        print("Archivo cargado en tableros correctamente . . .")
                        print("\n-----------------------------\n")
                    else:
                        print("\n-----------------------------\n")
                        print("Archivo no encontrado en /data, regresando . . .")
                        print("\n-----------------------------\n")
                # Cerrar juego
                case 0:
                    print("\n-----------------------------\n")
                    print("Cerrando juego")
                    print("\n-----------------------------\n")
                    break
                
                # Cualquier otro caso n (elección de tablero)
                case _:
                    iic2233.tablero_actual = opcion-2
                    print("\n-----------------------------\n")
                    print(f"Abriendo {iic2233.tableros[iic2233.tablero_actual]}")
                    print("\n-----------------------------\n")
                    menu_acciones(iic2233)

# -------------------------------------------------------------------        
# Menú de acciones para tablero escogido
# -------------------------------------------------------------------
def menu_acciones(instancia_dcc: DCColores):

    print("\n.\n.\n cargando . . . \n.\n.\n")
    while True:
        print("-----------------------------")

        print("-----------------------------")
        print("*** MENÚ DE ACCIONES ***\n")

        # Muestra de información de tablero actual

        print(instancia_dcc.tableros[instancia_dcc.tablero_actual])

        print(instancia_dcc.dibujar_tablero_actual())

        print(f"Cambios totales: {len(instancia_dcc.cambios_actuales)}")
        print(*instancia_dcc.cambios_actuales, sep=', ')

        # Validación de tablero completado o no
        if instancia_dcc.tableros[instancia_dcc.tablero_actual].validar_solucion(
            instancia_dcc.cambios_actuales):
            print("Tablero resuelto :D")
        else:
            print("Solución aún no encontrada")

        print("-----------------------------")
        print("[1] Agregar cambio")
        print("[2] Deshacer cambio")
        print("[3] Encontrar solución")
        print("[4] Guardar cambios")
        print("[5]  Volver al menú de Juego")
        print("-----------------------------")

        opcion = validar_opcion(1, 5)
        if opcion == -1:
            print("\n-----------------------------\n")
            print("Ingrese un valor válido dentro de los dados :D")
            print("\n-----------------------------\n")
        match opcion:
            # Agregar cambios
            case 1:
                print("\n-----------------------------\n")
                validar_coordx = input("Ingrese valor de x:")
                print("\n")
                validar_coordy = input("Ingrese valor de y:")
                print("\n-----------------------------\n")
                if validar_coordx.isdigit() and validar_coordy.isdigit():
                    posible_cambio = instancia_dcc.tableros[
                    instancia_dcc.tablero_actual].aceptar_posible_cambio(
                        int(validar_coordx), int(validar_coordy))
                    
                    if posible_cambio:
                        listado_coords = [int(validar_coordx), int(validar_coordy)]
                        print("\n-----------------------------\n")
                        instancia_dcc.agregar_cambio(listado_coords)
                        print("\n-----------------------------\n")
                    else:
                        print("\n-----------------------------\n")
                        print("No fue posible efectuar el cambio")
                        print("\n-----------------------------\n")
                pass
            # Deshacer cambios
            case 2:
                print("\n-----------------------------\n")
                instancia_dcc.deshacer_cambios()
                print("\n-----------------------------\n")
                
            # Encontrar solución para el tablero actual
            case 3:
                print("\n-----------------------------\n")
                print("Ingrese un valor para delimitar los cambios adicionales \n \
                      y poder encontrar solución a partir de aquello. . .")
                print("\n-----------------------------\n")
                cambios_pro = validar_opcion(1, 50)
                if cambios_pro == -1:
                    print("\n-----------------------------\n")
                    print("Valor no válido para ingreso de cambios adicionales, regresando . . .")
                    print("\n-----------------------------\n")
                else:
                    print("\n-----------------------------\n")
                    print("Buscando posible solución")
                    print("\n-----------------------------\n")
                    print(instancia_dcc.tableros[
                                            instancia_dcc.tablero_actual
                                            ].encontrar_solucion(
                                            instancia_dcc.cambios_actuales, 5))
            # Guardar archivo a partir de nombre del usuario
            case 4:
                print("\n-----------------------------\n")
                print("Ingrese un nombre de archivo para guardar sus cambios")
                print("Se borrará cualquier carácter prohibido que presente el ingreso \n"
                "dejando solo texto y valores númericos")
                print("Verificar únicamente el inicio del texto ingresado")
                print("\n-----------------------------\n")
                nombre_ingresado = validar_input()
                if nombre_ingresado == "invalid_name":
                    print("\n-----------------------------\n")
                    print("El nombre para archivo ingresado tiene un \
                          inicio NO válido, regresando. . .")
                    print("\n-----------------------------\n")
                else:
                    tablero_jugando = instancia_dcc.verificar_tablero_actual()
                    if tablero_jugando:
                        instancia_dcc.guardar_cambios(nombre_ingresado)
                        print("nombre de archivo guardado como ...")
                        print(f"{nombre_ingresado}.chg")
                    else:
                        pass

            # Volver al menú principal
            case 5:
                instancia_dcc.cambios_actuales.clear()
                break


if __name__ == "__main__":
    main()