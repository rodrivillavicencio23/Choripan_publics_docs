time = 145112
def convertime (time):
    hour = (time //10000)*60*60
    minu = ((time//100)%100)*60
    sec = (time%100)
    total = hour + minu + sec
    print(hour)
    print(minu)
    print(sec)
#NO USAR LO DE ARRIBA YA FUE APLICADO .
number = 19
def sumatoria (number):
    suma = 0
    for a in range(number+1):
        suma += a
    print(suma)
sumatoria(number)