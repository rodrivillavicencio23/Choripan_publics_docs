cell = int(input())
hour =int(input())
minu =int(input())
time = hour * 60 + minu
#Llamada entre 00:00 y las 8:20
if hour < 0:
    pass
else:
    if time <= 500:
        print("CONTESTAR EMERGENCIA")
    #Llamada entre 08:20 y las 13:00, si el número termina en 909 contestaer
    if time > 500 and time < 780:
            if (cell%1000) == 909:
                print("CONTESTAR 909")
            else:
                print("NO CONTESTAR 8:20-13:00")
    #Llamada entre 13:00 y las 19:50
    if time >= 780 and time <= 1190:
        if (cell//100000) == 877:
            print("NO CONTESTAR 877")                
        else:
            print("CONTESTAR 13:00-19:50")
    #Llamada entre las 19:50 y las 23:59
    if time > 1190 and time <=1440:
        print("NO CONTESTAR 19:50-00:00")