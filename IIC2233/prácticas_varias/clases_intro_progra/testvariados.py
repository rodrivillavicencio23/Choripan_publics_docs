
fila = [1,4,6]
fila2 = []

x = 4
alfa = 0

beta = 0
sigma = 0
def agregar(x,alfa,fila):
    for i in range(len(fila)):
        print(f"valor de i = {i}")
        if fila[i]>x:
            fila.insert(i,x)
            alfa = i
            return alfa
    

def agregar2(x,beta,fila):
    for i in range(len(fila)):
        print(f"valor de i = {i}")
        if fila[i]>x:
            fila.insert(i,x)
            beta = i
            return beta
    

seguir = True
while seguir:
    chelsea = input("Ingresa valor pe causa: ")
    if chelsea == "FIN":
        seguir = False
    else:
        chelsea = int(chelsea)

        alfa = agregar(chelsea,alfa,fila)
        print(fila)
        print(f"alfa = {alfa}")



        beta = agregar2(chelsea,beta,fila2)
        print(fila2)
        print(f"beta = {beta}")