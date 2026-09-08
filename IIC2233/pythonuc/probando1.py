fila_1 = []
fila_2 = []

def deter_pos(fila,cliente):
    for a in range (0,len(fila)):
        print(f"valor de a: {a}")
        if fila[a] > cliente:
            return a
    return len(fila)

seguir = True
#a mis reales socios les digo "Pri" (primo) :D
while seguir:
    x = input("ingresa valor pe causa:")
    if x == "FIN":
        seguir = False
    else:
        cliente = int(x)
        
        b = deter_pos(fila_1,cliente)
        c = deter_pos(fila_2,cliente)
        print(f"b = {b}")
        print(f"c = {c}")
        if b > c:
            print(f"La fila 1 es mejor para el nuevo cliente {cliente}")
            fila_1.insert(cliente,b)
        else:
            print(f"La fila 2 es mejor para el nuevo cliente {cliente}")
            fila_2.insert(cliente,c)
            
    print("Nuevas filas:")
    print(fila_1)
    print(fila_2)