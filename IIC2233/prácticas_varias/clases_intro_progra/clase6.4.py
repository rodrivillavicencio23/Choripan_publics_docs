rut = int(input("ingrese rut: "))
exp = 1
div = 10
nrut = 8
ini = 3
suma = 0
#print(rut//exp%10)
#print(rut//(exp*10)%10)
while nrut != 0:
    digito= (rut//exp%div)
    digito = digito * ini
    print (digito)
    exp = (exp*10)
    nrut-=1
    if ini !=1:
        suma+=digito
        ini=1
    elif ini == 1:
        ini = 7

print(suma)

