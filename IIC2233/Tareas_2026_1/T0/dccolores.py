# -------------------------------------------------------------------
# Imports y modularización
from tablero import Tablero
from visualizador import tablero_a_texto
from pathlib import os, Path

class DCColores:
    def __init__(self) -> None:
        self.tableros: list[Tablero] = []
        self.tablero_actual = -1
        self.cambios_actuales = []


    def cargar_tablero(self, archivo_tablero: str) -> None:
        """ 
        Recibe un texto con el nombre del archivo que contiene el tablero. 
        Crea una instancia de Tablero
        con la información correspondiente y 
        la agrega al final de la lista self.tablero.

        """
        ruta = os.path.join("data", archivo_tablero + ".brd")
        with open (ruta, "r", encoding="UTF-8") as lista_archivo:
            primera_linea = lista_archivo.readline().split()
            ene = int(primera_linea[0])
            eme =  int(primera_linea[1])
            lista_transf = []
            for linea in lista_archivo:
                nueva_linea = linea.rstrip('\n')
                if nueva_linea == "":
                    pass
                # dividir el string en lista
                sublista = list(nueva_linea)
                fila_nums = []
                # reemplazo de valores a 'ints'
                for dig in sublista:
                    if dig == "_":
                        fila_nums.append(0)
                    elif dig == "#":
                        fila_nums.append(1)
                    elif dig == "O":
                        fila_nums.append(-1)
                
                lista_transf.append(fila_nums)
            
            inicio = lista_transf[:ene]
            meta   = lista_transf[ene:]
            
            nuevo_tablero = Tablero(inicio, meta)
            nuevo_tablero.n_tab = ene
            nuevo_tablero.m_tab = eme
            self.tableros.append(nuevo_tablero)

    def verificar_tablero_actual(self) -> True | False:
        if self.tablero_actual == -1:
            print("No hay tablero para guardar, regresando ...")
            return False
        return True

    def guardar_cambios(self, nombre_archivo: str) -> None:
        
        verif = self.verificar_tablero_actual()
        if verif:
        
            archivo_extendido = f"{nombre_archivo}.chg"
            ruta = os.path.join("data", archivo_extendido)
            with open(ruta, "w", encoding="UTF-8") as guardar_archivo:
                
                ene = self.tableros[self.tablero_actual].n_tab
                eme = self.tableros[self.tablero_actual].m_tab
                n_cambios = len(self.cambios_actuales)
                guardar_archivo.write(f"{ene} {eme} {n_cambios}\n")

                tablero_de_inicio = tablero_a_texto(
                    self.tableros[self.tablero_actual].inicio, "texto")
                guardar_archivo.write(f"{tablero_de_inicio}")

                for i in range(len(self.cambios_actuales)):
                    coord_x = self.cambios_actuales[i][0]
                    coord_y = self.cambios_actuales[i][1]
                    guardar_archivo.write(f"{coord_x} {coord_y}\n")
                    
                    tablero_c = self.tableros[self.tablero_actual].aplicar_cambios(
                        self.cambios_actuales[:i+1]
                    )
                    tablero_texto = tablero_a_texto(tablero_c, "texto")
                    guardar_archivo.write(f"{tablero_texto}")

                guardar_archivo.write("\n")
    
    def agregar_cambio(self, coords: tuple[int, int]):
        self.cambios_actuales.append(coords)
        print("Cambio añadido a la lista")
        return

    def deshacer_cambios(self) -> None:
        if len(self.cambios_actuales) == 0:
            print("No hay cambios para deshacer brother")
            return 
        self.cambios_actuales.pop()
        print("Ultimo movimiento borrado correctamente")
        return
    

    def dibujar_tablero_actual(self):
        if self.verificar_tablero_actual():
            print("Meta: \n")
            print(tablero_a_texto(self.tableros[self.tablero_actual].meta, "emoji"))
            print("Estado Actual: \n")
            
            print(tablero_a_texto(self.tableros[self.tablero_actual].aplicar_cambios(self.cambios_actuales), "emoji"))
            return f". . ."
        return f"No hay tablero cargado (¿cómo llegaste hasta aquí, imposible?)"
    

    """
    Recordatorio acerca de tablero_a_texto:
    
    tablero_a_texto(tablero: list[list[int]], modo: str) -> str.
    Recibe una lista de listas de números con el estado de un tablero y un string que indica el modo de
    representación del tablero. Entrega la representación como texto de un tablero recibido.

    Modos:
    color
    emoji (seleccioné este)
    texto

    
    """