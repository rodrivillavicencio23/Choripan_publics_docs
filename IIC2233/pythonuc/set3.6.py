baseforce = int(input())
obj = int(input())
golpes = 0
elevado = 1
a=0
expresion = ""
valor = 1
signo = 1
print("1 = 1")
while valor < obj:

    golpes+=1
    #Intercalar signos APROBADA
    if signo == 1:
        signo = -1
    elif signo == -1:
        signo = 1
    #Fórmula APROBADA
    a = signo * (baseforce**elevado)
    valor += a
    elevado +=1
    
    expresion = (f"{expresion} + {a}")
    print(f"1{expresion} = {valor}")
    

print(f"Necesite {golpes+1} golpes para alcanzar los {obj} metros")
    #cabrontunoveeeese