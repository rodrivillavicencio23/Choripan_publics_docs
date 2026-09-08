numero = 19822
a = len(str(numero))
digitos = 4
dif_digitos = a-digitos

nsector = ""
def encri_par(numero,a,nsector):
    sector = str(numero)[dif_digitos:a]
    print(sector)
    for xd in sector:
        b = int(xd)+2
        c = b**b
        print(c)
        d = len(str(c))
        e = str(c)[d-1]
        print(e)
        nsector+=e
        print(nsector)
    print(numero-int(sector)+int(nsector))

def encri_impar(numero,a,nsector,digitos):
    sector = str(numero)[0:digitos]
    q_sector = sector[::-1]
    print("vamos a encriptar:",sector)
    for xd in sector:
        print("número: ",xd)
        b = int(xd)+2
        c = b**b
        print("resultado + 2 elevado a si mismo: ",c)
        d = len(str(c))
        e = str(c)[d-1]
        print("último dígito: ",e)
        nsector+=e
        print("sector hasta ahora: ",nsector)
    nsector_2 = nsector[::-1]
    print("sector inverso: ", nsector_2)
    f = str(numero)[::-1]
    g = int(f)-int(q_sector)+int(nsector_2)
    h = str(g)[::-1]
    print(int(h))

if digitos > 0: 
    if a % 2 ==0:
        encri_par(numero,a,nsector)  
    elif a % 2 == 1:
        encri_impar(numero,a,nsector,digitos)  
else:
    print(numero)