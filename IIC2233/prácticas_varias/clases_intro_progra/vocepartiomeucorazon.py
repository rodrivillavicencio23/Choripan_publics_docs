
def contraimpar (xd,str_sector):
    
    nuevo_sector = ""
    for a in str(str_sector):
        b = (int(a)+2)
        c = b**b
        d = c %10
        nuevo_sector = (f"{nuevo_sector+str(d)}")
        nuevo_sector_inverso = str(nuevo_sector)[::-1]
        q = int(f)-int(i)+int(nuevo_sector)
        resultado = str(q)[::-1]
    print(int(resultado))
    return

def contrapar (xd,str_sector):
    nuevo_sector = ""
    for a in str(str_sector):
        b = (int(a)+2)
        c = b**b
        d = c %10
        nuevo_sector = (f"{nuevo_sector+str(d)}")
    print(xd-int(sector)+int(nuevo_sector))
    return


#NO TOCAR
xd = int(input())
digitos = int(input())
len_digitos = len(str(xd))
sector = 0

if len_digitos % 2 == 0:
    sector = xd % (10**(digitos))
    str_sector = str(sector)
    contrapar(xd,str_sector)
    
elif len_digitos % 2 == 1:
    f = str(xd)[::-1]
    sector = str(xd)[0:digitos]
    h = str(sector)
    i = str(sector)[::-1]
    str_sector = str(sector)
    contraimpar(xd,i)