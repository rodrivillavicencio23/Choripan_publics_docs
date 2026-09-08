"""
nombre = "agustin villavicencio"

lista_nombre = list(nombre)
print(lista_nombre)

xd = "".join(lista_nombre)
print(xd)

print(nombre[0])
"""
import os

from visualizador import tablero_a_texto

tablero = [[-1, 1, -1, 0], 
           [1, -1, 1, -1], 
           [0, 1, -1, 1]]

print(tablero_a_texto(tablero, "emoji"))

def cambiar_posicion(tablero: list[list[int]], cambio: tuple[int]):
    cord_x = cambio[0]
    cord_y = cambio[1]

    if (cord_x > len(tablero) or cord_x < 0) or (cord_y > len(tablero[0]) or cord_y < 0):
        print(f"Coordenada fuera de rango del tablero")
    else:
        for a in range(cord_x-1, cord_x+2):
            for b in range(cord_y-1, cord_y+2):
                
                if (a < 0 or a >= len(tablero)) or (b < 0 or b >= len(tablero[0])):
                    pass
                else:
                    print(a, b)
                    pos = tablero[a][b]
                    if pos == 1:
                        tablero[a][b] = -1
                    elif pos == -1:
                        tablero[a][b] = 1


cambiar_posicion(tablero, (1, 0))


print(tablero_a_texto(tablero, "emoji"))


ruta = os.path.join("data", "tablero_5")

if ruta:
    print(ruta)

for l in tablero:
    for c in l:
        print(c, end= " ")
    print() 