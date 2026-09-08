historial = input()
time = 0 #Frecuencia más larga
final_time = 0 #Inicio de esa frecuencia
minute = 0 
frec_start = 0
des_actual = 0

for xd in historial:
    if xd == "F":
        if time == 0:
            des_actual = minute
            
        time+=1
    elif xd == "D":
        time=0
    #no cambiar
    minute+=1
    print("Minuto: ",minute)

    if time > final_time:
        final_time = time
        print(f"Frecuencia más larga es de:{final_time}")
        frec_start = des_actual
        print(f"Frecuencia más larga inicio a los: {frec_start}")

print(f"La desconexion mas larga duro {final_time} minutos y comenzo al minuto {frec_start}")