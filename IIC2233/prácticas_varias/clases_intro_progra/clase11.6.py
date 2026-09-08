#Clase 11.6

def numero_lagartijas():
    i = 0
    seguir = True
    while seguir:
        e =existe_lagartija(i)
        if e == False:
            i += 0
            print(i)
            return
        elif e == True:
            i +=1