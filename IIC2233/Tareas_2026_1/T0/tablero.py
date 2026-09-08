# -------------------------------------------------------------------
# Imports y modularización
from copy import deepcopy

# -----------------------------------------------------------------------------
# Clase Tablero
# -----------------------------------------------------------------------------
class Tablero:
    def __init__(self, inicio: list[tuple[int]], meta: list[tuple[int, int]]) -> None:
        self.inicio = inicio
        self.meta = meta
        self.n_tab = len(inicio)
        self.m_tab = len(inicio[0])

    # Completado: cambiar color de posición (x,y) y sus vecinos
    def cambiar_color(self, tablero_actual: list[list[int, int]],
                      x: int, y: int) -> list[list[int]]:

        tablero_mod = deepcopy(tablero_actual)
        if (x > len(tablero_mod) or x < 0) or \
            (y > len(tablero_mod[0]) or y < 0):
            print(f"Coordenada fuera de rango del tablero")
        else:
            # recorrer sublistas
            for a in range(x-1, x+2):
                # recorrer dentro de cada sublista
                for b in range(y-1, y+2):
                    
                    if (a < 0 or a >= len(tablero_mod)) or \
                      (b < 0 or b >= len(tablero_mod[0])):
                        pass
                    elif tablero_mod[a][b] == 0:  
                        pass
                    else:
                        pos = tablero_mod[a][b]
                        if pos == 1:
                            tablero_mod[a][b] = -1
                        elif pos == -1:
                            tablero_mod[a][b] = 1
            return tablero_mod

    # Completado: aplicar cambios a partir de una lista de tuplas/listas de cambios
    def aplicar_cambios(self, cambios: list[list[int]]) -> list[list[int]]:
        tablero_copia = deepcopy(self.inicio)
        for cambio in cambios:
            x_coord = cambio[0]
            y_coord = cambio[1]
            tablero_copia = self.cambiar_color(tablero_copia, x_coord, y_coord)
        return tablero_copia
    # -------------------------------------------------------------------------
    # Completado: validar que los cambios llegan a una solución
    # -------------------------------------------------------------------------
    def validar_solucion(self, cambios: list[tuple[int]]) -> bool:
        posible_solucion = self.aplicar_cambios(cambios)
        if posible_solucion == self.meta:
            return True
        else:
            return False
    # -------------------------------------------------------------------------
    # Completado: Encontrar una solución mediante Backtracking y devolver una lista
    # -------------------------------------------------------------------------
    def encontrar_solucion(self, cambios: list[tuple[int]],
                           cambios_adicionales: int) -> list[tuple[int]]:
        if self.validar_solucion(cambios):
            return cambios
        if cambios_adicionales == 0:
            return []
        
        for ene in range(self.n_tab):
            for eme in range(self.m_tab):
                if self.inicio[ene][eme] != 0:
                    cambios_nuevos = cambios + [(ene, eme)]   
                    resultado = self.encontrar_solucion(cambios_nuevos, (cambios_adicionales - 1))
                    if resultado != []:
                        return resultado
        return []
    # -------------------------------------------------------------------------
    # No completado (2/5): Eliminar redundancias de encontrar solución
    # -------------------------------------------------------------------------
    def optimizar_solucion(self, cambios: list[tuple[int, int]]) -> list[tuple[int, int]]:
        cambios_copia = list(cambios)
        i = 0
        while i < len(cambios_copia):
            lista_acotada = cambios_copia[:i] + cambios_copia[i+1:]
            
            if self.validar_solucion(lista_acotada):
                cambios_copia = lista_acotada
            else:
                i += 1
        return cambios_copia
    
    # -------------------------------------------------------------------------
    # Verificar que un cambio es apto para aplicarlo en el tablero
    # -------------------------------------------------------------------------
    def aceptar_posible_cambio(self, x:int, y:int):
        """
        Retorna valor de verdad si es que x e y
        están dentro del rango
        """
        if (x > self.n_tab or y > self.m_tab) or \
            (x < 0 or y < 0):
            return False
        return True
    
    # -------------------------------------------------------------------------
    # Printear información de N x M del tablero
    # -------------------------------------------------------------------------
    def __str__(self):
        return f"Tablero {self.n_tab}x{self.m_tab}"
