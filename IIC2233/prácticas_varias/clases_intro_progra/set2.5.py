cell = int(input())
hour =int(input())
minu =int(input())


#Llamada entre 00:00 y las 8:20
#Listo
if (hour < 8 and minu <=59) or (hour == 8 and minu <=20):
    print("CONTESTAR EMERGENCIA")

#Llamada entre 08:20 y las 13:00, si el número termina en 909 contestaer
#Listo
if (hour >= 8 and minu > 20 and hour < 13) or (hour > 8 and hour < 13 and minu <=59):
        if (cell%1000) == 909:
            print("CONTESTAR 909")
        else:
            print("NO CONTESTAR 8:20-13:00")

#Llamada entre 13:00 y las 19:50
#Listo
if (hour >= 13 and minu >= 0 and hour < 19) or ( hour >= 13 and hour <= 19 and minu <=50):
    if (cell//100000) == 877:
        print("NO CONTESTAR 877")                
    else:
        print("CONTESTAR 13:00-19:50")


#Llamada entre las 19:50 y las 23:59
#Listo
if(hour >= 19 and minu > 50) and ( hour <= 23 and minu <= 59):
    print("NO CONTESTAR 19:50-00:00")