
# -----------------------------------------------------------------------------
# Imports y modularización
from helpers_2 import (validar_nombre_archivo
                       , validar_opcion
                ,validar_en_data, tirar_dados, validar_input)
from dcclue import Dcclue
from main_2 import menu_consulta, menu_habitacion
from sys import exit
# -----------------------------------------------------------------------------
# Menús de juego
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# Menú principal
# -----------------------------------------------------------------------------
lista_partidas = []
def main():
    print("\n.\n.\n cargando ... \n.\n.\n")
    while True:
        print("\n-----------------------------")
        print("-----------------------------\n")
        print("\n MENÚ PRINCIPAL\n")
        
        print("-----------------------------")
        print("[1] Crear nueva partida")
        print("[2] Cargar partida existente")

        for num ,table in enumerate(lista_partidas, start=3):
            print(f"[{num}] {table}")

        print("\n[0] Salir del programa")
        print("-----------------------------")

        opcion = validar_opcion(0, 2 + len(lista_partidas))
        if opcion == -1:
            print("\n-----------------------------\n")
            print("Ingrese un valor válido dentro de los dados :D")
            print("\n-----------------------------\n")
        else:
        
            match opcion:
                # Abrir tablero a partir de input del usuario
                case 1:
                    print("\n-----------------------------\n")
                    print("Creando nueva partida . . .")
                    print("\n-----------------------------\n")
                    nueva_instancia_dcc = Dcclue(None)
                    nueva_instancia_dcc.estado.cargar_datos()
                    nueva_instancia_dcc.inicializar_estado()
                    
                    lista_partidas.append(nueva_instancia_dcc)
                    menu_dcclue(nueva_instancia_dcc)
                case 2:
                    print("\n-----------------------------\n")
                    print("Ingrese el nombre del archivo sin la extensión de este:")
                    print("\n-----------------------------\n")

                    nombre_archivo_abrir = input(">>>>>>>>")
                    valido = validar_en_data(nombre_archivo_abrir)
                    if valido:
                        # HERE : ARCHIVO GUARDADO
                        instancia_dcc = Dcclue(None)
                        lista_partidas.append(instancia_dcc)
                        print("\n-----------------------------\n")
                        print("Archivo cargado correctamente . . .")
                        print("\n-----------------------------\n")
                    else:
                        print("\n-----------------------------\n")
                        print("Archivo no encontrado en /data, regresando . . .")
                        print("\n-----------------------------\n")
                # Cerrar juego
                case 0:
                    print("\n-----------------------------\n")
                    print("Cerrando juego . . .")
                    print("Saludos . . .")
                    print("\n-----------------------------\n")
                    # romper todo
                    exit()
                
                # Cualquier otro caso n (elección de tablero)
                case _:
                    print("\n-----------------------------\n")
                    print(f"Abriendo Partida seleccionada. . .")
                    print("\n-----------------------------\n")
                    menu_dcclue(lista_partidas[opcion-3])
                    
# -------------------------------------------------------------------        
# Menú de acciones para tablero escogido
# -------------------------------------------------------------------
def menu_dcclue(instancia_dcc: Dcclue):
    # Si el jugador presiona Enter se asigna un nombre predeterminado
    nombre_jug = input("Ingrese nombre de jugador. . .")
    if nombre_jug == "":
        nombre_jug = "Jugador_1"
    
    instancia_dcc.nombre_jugador = nombre_jug
    print("\n.\n.\n cargando . . . \n.\n.\n")
    while True:
        print("-----------------------------")
        print("*** MENÚ DCClue ***\n")
        print(f"Username: {instancia_dcc.nombre_jugador} \n")
        print(f"Personaje asignado: {instancia_dcc.estado.personaje_jugador._nombre}")
        print(f"Rondas Jugadas: {instancia_dcc.estado.rondas_jugadas}")
        print("-----------------------------")
        print("[1] Tirar los dados")
        print("[2] Historial de consultas")
        print("[3] Guardar partida")
        print("[4] Adivinar Asesinato")
        print("[5] Mostrar Informacion")
        print("\n[0] Volver a inicio")
        print("-----------------------------")
        opcion = validar_opcion(0, 5)
        if opcion == -1:
            print("\n-----------------------------\n")
            print("Ingrese un valor válido dentro de los dados :D")
            print("\n-----------------------------\n")
        match opcion:
            # Tirar los dados
            case 1:
                print("\n-----------------------------\n")
                print("Tirando Dados . . .")
                print("\n-----------------------------\n")
                menu_turno(instancia_dcc)
            
            # Historial de consultas
            case 2:
                print("\n-----------------------------\n")
                print("NO IMPLEMENTADO")
                print("\n-----------------------------\n")
                pass
                
            # Guardar partida a partir de nombre del usuario
            case 3:
                print("\n-----------------------------\n")
                print("NO IMPLEMENTADO")
                print("\n-----------------------------\n")
    
            # Adivinar Asesinato
            case 4:
                print("\n-----------------------------\n")
                print("Yendo a menú acusación . . .")
                print("\n-----------------------------\n")
                menu_acusacion(instancia_dcc)

            # Mostrar Información
            case 5:
                print("\n-----------------------------\n")
                print("NO IMPLEMENTADO")
                print("\n-----------------------------\n")
                pass

            # Volver al menú principal
            case 0:
                break

# -----------------------------------------------------------------------------
# Menú de turno: cuando el jugador tira los dados : READY BRO
# -----------------------------------------------------------------------------
def menu_turno(instancia_dcc: Dcclue):

    print("\n.\n.\n cargando . . . \n.\n.\n")
    while True:
        print("-----------------------------")
        dado_1, dado_2 = tirar_dados()
        print(f"Resultados Dados: ")
        print(f"Dado 1: {dado_1} | Dado 2: {dado_2}")
        print("-----------------------------")
        print("*** MENÚ TURNO ***\n")
        print("-----------------------------")
        print("Acciones disponibles:\n")
        
        if dado_1 == dado_2:
            print("Opciones iguales:")
        print(f"""[1] Mover a habitación ({dado_1})
        {instancia_dcc.estado.obtener_habitacion_indice(dado_1)}
        """)
        
        print(f"""[2] Mover a habitación ({dado_2})
        {instancia_dcc.estado.obtener_habitacion_indice(dado_2)}
        """)
        print("-----------------------------")

        opcion = validar_opcion(1, 2)
        if opcion == -1:
            print("\n-----------------------------\n")
            print("Ingrese un valor válido dentro de los dados :D")
            print("\n-----------------------------\n")
        match opcion:
            
            case 1:
                print("\n-----------------------------\n")
                print(f"""
                      Moviéndose a {instancia_dcc.estado.obtener_habitacion_indice(dado_1)}
                        """)
                print("\n-----------------------------\n")
                instancia_dcc.estado.mover_habitacion_indice(dado_1)
                menu_habitacion(instancia_dcc, pasadizo_ocupado=False)
                
            case 2:
                print("\n-----------------------------\n")
                print(f"""
                    Moviéndose a {instancia_dcc.estado.obtener_habitacion_indice(dado_2)}
                    """)
                print("\n-----------------------------\n")
                instancia_dcc.estado.mover_habitacion_indice(dado_2)
                return menu_habitacion(instancia_dcc, pasadizo_ocupado=False)
                
# -----------------------------------------------------------------------------
# Menú de acusación para encontrar culpable
# -----------------------------------------------------------------------------
def menu_acusacion(instancia_dcc: Dcclue):
    personaje = None
    habitacion = None
    arma = None
    print("\n.\n.\n cargando . . . \n.\n.\n")
    while True:
        print("-----------------------------")
        print(f"Nombre: {instancia_dcc.nombre_jugador}")
        print(f"Personaje asignado: {instancia_dcc.estado.personaje_jugador._nombre}")
        print("-----------------------------")
        print("*** MENÚ ACUSACIÓN ***\n")
        print("-----------------------------")
        print("Realiza tu acusacion para \n finalizar el juego.")
        print("Acusacion:")
        print(f"- Sospechoso: {personaje}")
        print(f"- Arma:  {arma}")
        print(f"- Habitacion: {habitacion}")
        print("[1] Elegir sospechoso")
        print("[2] Elegir arma")
        print("[3] Elegir habitacion")
        print("[4] Realizar acusacion")
        print("[5] Volver al menu anterior")
        print("-----------------------------")
        opcion = validar_opcion(1, 5)
        if opcion == -1:
            print("\n-----------------------------\n")
            print("Ingrese un valor válido dentro de los dados :D")
            print("\n-----------------------------\n")
        match opcion:
            # Elegir sospechoso
            case 1:
                print("\n-----------------------------\n")
                print("Eliga al sospechoso")
                print("\n-----------------------------\n")
                verdad, nombre_adivinar = validar_input()
                if verdad:
                    personaje = nombre_adivinar
                    continue
                else:
                    print("\n-----------------------------\n")
                    print(f"Entrada inválida ! ERROR : {nombre_adivinar}")
                    print("\n-----------------------------\n")
                
            # Elegir arma
            case 2:
                print("\n-----------------------------\n")
                print("Eliga la arma usada para el crimen")    
                print("\n-----------------------------\n")
                verdad, arma_adivinar = validar_input()
                if verdad:
                    arma = arma_adivinar
                    continue
                else:
                    print("\n-----------------------------\n")
                    print(f"Entrada inválida ! ERROR : {arma_adivinar}")
                    print("\n-----------------------------\n")
                
            # Elegir habitacion
            case 3:
                print("\n-----------------------------\n")
                print("Eliga la habitación donde fue el asesinato")
                print("\n-----------------------------\n")
                verdad, hab_adivinar = validar_input()
                if verdad:
                    habitacion = hab_adivinar
                    continue
                else:
                    print("\n-----------------------------\n")
                    print(f"Entrada inválida ! ERROR : {hab_adivinar}")
                    print("\n-----------------------------\n")
                 
            # Realizar acusacion
            case 4:
                if not (personaje is None) and not \
                    (habitacion is None) and not (arma is None):

                    print("\n-----------------------------\n")
                    resultado_final = instancia_dcc.estado.validar_acusacion(
                        personaje, arma, habitacion)

                    menu_resultado(instancia_dcc, resultado_final)
                    print("\n-----------------------------\n")
                else:
                    print("\n-----------------------------\n")
                    print("No haz hecho la acusación completa, regresando ...")
                    print("\n-----------------------------\n")

            # Volver al menu anterior
            case 5:
                print("\n-----------------------------\n")
                print("Regresando al menú anterior")    
                print("\n-----------------------------\n")
                break              
# -----------------------------------------------------------------------------
# Menú de resultado final: Ganado o perdido
# -----------------------------------------------------------------------------
def menu_resultado(instancia_dcc: Dcclue, resultado: bool):
    print("\n.\n.\n cargando . . . \n.\n.\n")
    while True:
        print("-----------------------------")
        print("*** RESULTADOS DE PARTIDA ***\n")
        print("-----------------------------")
        final = "Perdido"
        if resultado:
            final = "Ganado"
        print(f"Haz {final}!")
        print(f"Asesino: {instancia_dcc.datos_asesino()}")
        print("-Acciones disponibles:")
        print("[1] Historial de consultas")
        print("[2] Volver al Menú de inicio")
        print("-----------------------------")

        opcion = validar_opcion(1, 2)
        if opcion == -1:
            print("\n-----------------------------\n")
            print("Ingrese un valor válido dentro de los dados :D")
            print("\n-----------------------------\n")
        match opcion:
            # Elegir sospechoso
            case 1:
                print("\n-----------------------------\n")
                print("NO IMPLEMENTADO . . .")
                print("\n-----------------------------\n")
                pass
            case 2:
                print("\n-----------------------------\n")
                print("Regresando al menú inicial . . .")
                print("\n-----------------------------\n")
                main()
 
# -----------------------------------------------------------------------------
# Inicializador archivo main.py y menú main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
# -----------------------------------------------------------------------------