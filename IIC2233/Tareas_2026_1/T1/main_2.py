
# -----------------------------------------------------------------------------
# Imports y modularización
from helpers_2 import (validar_nombre_archivo
                       , validar_opcion
                ,validar_en_data, tirar_dados, validar_input)
from dcclue import Dcclue

# -----------------------------------------------------------------------------
# Menú de habitación : Cuando se mueve a habitación u ocupa 
# pasadizo secreto
# -----------------------------------------------------------------------------
def menu_habitacion(instancia_dcc: Dcclue, pasadizo_ocupado: bool):
    print("\n.\n.\n cargando . . . \n.\n.\n")
    estado = instancia_dcc.estado
    habitacion = estado.habitacion_actual

    while True:
        print("-----------------------------")
        print(f"Jugador: {instancia_dcc.nombre_jugador}")
        print("-----------------------------")
        print("*** MENÚ HABITACION ***")
        print("-----------------------------")
        print(f"Te encuentras en la habitación: {habitacion.nombre}\n")
        
        sospechoso_actual = estado.obtener_sospechoso_habitacion_actual()
        if sospechoso_actual == None:
            print("No hay ningun sospechoso en esta habitacion.\n")
        else:
            print(f"Sospechoso en la habitacion: {sospechoso_actual._nombre}\n")

        print("-Acciones disponibles:")        
        if sospechoso_actual != None:
            print("[1] Hacer una consulta al sospechoso")
        else:
            print("[1] Hacer una consulta al sospechoso (no disponible)")

        print("[2] Ver pistas")

        if habitacion.pasadizo and not pasadizo_ocupado:
            print(f"[3] Usar pasaje secreto -> {habitacion.pasadizo}")
        elif pasadizo_ocupado:
            print("[3] Usar pasaje secreto (ya usado en este turno)")
        else:
            print("[3] Usar pasaje secreto (no disponible)")


        opcion = validar_opcion(1, 3)
        if opcion == -1:
            print("\n-----------------------------\n")
            print("Ingrese un valor válido dentro de los dados :D")
            print("\n-----------------------------\n")
        match opcion:
            # Elegir sospechoso
            case 1:
                
                if sospechoso_actual is None:
                    print("\n-----------------------------\n")
                    print("""No hay sospechoso para  \n 
                        consultar en esta habitacion""")
                    print("\n-----------------------------\n")
                else: 
                    print("\n-----------------------------\n")
                    print("Yendo a menú de consulta . . .")
                    print("\n-----------------------------\n")
                    menu_consulta(instancia_dcc)
                    return
                
            # Elegir arma
            case 2:
                print("\n-----------------------------\n")
                print("NO IMPLEMENTADO . . .")
                print("\n-----------------------------\n")
                pass  
            case 3:
                if pasadizo_ocupado:
                    print("\n-----------------------------\n")
                    print("El pasadizo para el turno ya ha sido ocupado!")
                    print("\n-----------------------------\n")
                elif habitacion.pasadizo == "-":
                    print("\n-----------------------------\n")
                    print("No hay pasadizo disponible !")
                    print("\n-----------------------------\n")
                else:
                    print("\n-----------------------------\n")
                    print(f"Usando pasadizo secreto . . .")
                    print("\n-----------------------------\n")
                    instancia_dcc.estado.usar_pasaje_secreto()
                    return menu_habitacion(instancia_dcc, pasadizo_ocupado=True)
                
# -----------------------------------------------------------------------------
# Menú de consulta : Preguntar por arma o sospechoso
# -----------------------------------------------------------------------------
def menu_consulta(instancia_dcc: Dcclue):

    print("\n.\n.\n cargando . . . \n.\n.\n")
    while True:
        print("-----------------------------\n")
        print(f"Jugador: {instancia_dcc.nombre_jugador}")
        print("-----------------------------")
        print("*** MENÚ CONSULTA ***\n")
        print("-----------------------------")
        print(f"""
            - Realiza tu consulta -
            {instancia_dcc.estado.obtener_sospechoso_habitacion_actual()}
            """)

        print("-----------------------------")
        print("\n- Consulta:\n")
        print("-----------------------------")
        print(f"- Sospechoso: {instancia_dcc.estado.habitacion_actual.sospechoso}")
        print(f" - Arma: ")
        # HERE
        print("-Acciones disponibles:")
        print("[1] Elegir sospechoso")
        print("[2] Elegir arma")
        print("[3] Realizar consulta")
        print("[4] Volver al menu anterior")
        print("-----------------------------")

        opcion = validar_opcion(1, 4)
        if opcion == -1:
            print("\n-----------------------------\n")
            print("Ingrese un valor válido dentro de los dados :D")
            print("\n-----------------------------\n")
        match opcion:
            # Elegir sospechoso
            case 1:
                print("\n-----------------------------\n")

                print("\n-----------------------------\n")
                pass

            # Elegir arma
            case 2:
                print("\n-----------------------------\n")
                
                print("\n-----------------------------\n")
                pass  
            case 3:
                print("\n-----------------------------\n")
                
                print("\n-----------------------------\n")
                pass
            case 4:
                print("\n-----------------------------\n")
                print("Regresando al menú anterior")
                print("\n-----------------------------\n")
                break

