historial = input()
#D conexión
#F desconexión
time = 0 # Frecuencia más larga actual
final_time = 0 # Duración de la desconexión más larga
minute = 0
frec_start = 0
start_current_disconnect = 0  # NUEVA VARIABLE para registrar inicio de cada desconexión

for xd in historial:

    if xd == "F":
        if time == 0:
            start_current_disconnect = minute  # Guardamos minuto donde empieza esta desconexión
        time += 1
        conexion = False
    
    elif xd == "D":
        time = 0
        print(frec_start)

    if time > final_time:
        final_time = time
        frec_start = start_current_disconnect  # Aquí actualizamos con el inicio real de la desconexión más larga
        print(final_time)
    
    minute += 1
    print("minuto:", minute)

print(f"La desconexion mas larga duro {final_time} minutos y comenzo al minuto {frec_start}")
