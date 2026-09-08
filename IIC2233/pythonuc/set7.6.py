tablero = [
    ["X","O","O"],
    ["X","-","O"],
    ["X","X","-"]
]



def mostrar_estado_gato(tablero):
    
    ganador = "Empate"

    print("filas --->")
    #filas
    for a in tablero:
        print("------------")
        print(a[0],a[1],a[2])
        if a[0] == a[1] == a[2] != "-":
            ganador = a[0]
    
    print("columnas V")
    for b in range(0,3):
        print("------------")
        print(tablero[0][b])
        print(tablero[1][b])
        print(tablero[2][b])
        if tablero[0][b] == tablero[1][b] == tablero[2][b] != "-":
            ganador = tablero[0][b]
    
    #Diagonales
        if tablero[0][0] == tablero[1][1] == tablero[2][2]:
            ganador = tablero[0][0]

    #Ganador
    if ganador == "O" or ganador == "X":
        print(f"ganador: {ganador}")
    else:
        print(f"No ha terminado")

mostrar_estado_gato(tablero)