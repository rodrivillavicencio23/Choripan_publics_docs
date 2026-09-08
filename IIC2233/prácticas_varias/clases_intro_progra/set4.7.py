
def contraimpar (xd,str_sector):
    
    nuevo_sector = ""
    for a in str(str_sector):
        print("digito", a)
        b = (int(a)+2)
        print("b = ",b)
        c = b**b
        print("b ** b =",c)
        d = c %10
        print(f"último dígito: {d}")
        nuevo_sector = (f"{nuevo_sector+str(d)}")
        nuevo_sector_inverso = str(nuevo_sector)[::-1]
        print(nuevo_sector)
        q = int(f)-int(i)+int(nuevo_sector)
        resultado = str(q)[::-1]
    print(int(resultado))
    return


def contrapar (xd,str_sector):
    
    nuevo_sector = ""
    for a in str(str_sector):
        print("digito", a)
        b = (int(a)+2)
        print("b = ",b)
        c = b**b
        print("b ** b =",c)
        d = c %10
        print(f"último dígito: {d}")
        nuevo_sector = (f"{nuevo_sector+str(d)}")
        print(nuevo_sector)
    print(xd-int(sector)+int(nuevo_sector))
    return


#NO TOCAR
xd = int(input())
digitos = int(input())
len_digitos = len(str(xd))
sector = 0


if len_digitos % 2 == 0:
    sector = xd % (10**(digitos))
    print(sector)
    str_sector = str(sector)
    contrapar(xd,str_sector)
    
elif len_digitos % 2 == 1:
    print("se metio en impar")
    f = str(xd)[::-1]
    print("tamos tomando",f)
    sector = str(xd)[0:digitos]
    print("tamos tomando: ",sector)
    h = str(sector)
    print(h)
    i = str(sector)[::-1]
    print(i)
    
    str_sector = str(sector)
    contraimpar(xd,i)

