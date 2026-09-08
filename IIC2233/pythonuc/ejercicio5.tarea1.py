nombre = input()
weight_car = int(input())


#PREGUNTA 1
print(f"Bienvenid@ a la carrera {nombre}")

if weight_car < 50:
    print("Tienes un auto liviano")
    categoria = 1
elif weight_car >= 50 and weight_car < 100:
    print("Tienes un auto mediano")
    categoria = 2
else:
    print("Tienes un auto pesado")
    categoria = 3


#PREGUNTA 2
n = int(input())
m = 0
velocidad_final = 0
while m < n:
    rango1 = int(input())
    rango2= int(input())
    velocidad = int(input())
    if weight_car >= rango1 and weight_car <= rango2:
        print(f"Ligereza valida para el neumatico de velocidad {velocidad}")
        if velocidad > velocidad_final:
            velocidad_final = velocidad
            print(f"Tu nueva velocidad es {velocidad_final}")
    m+=1
print(f"Tu velocidad para la carrera sera {velocidad_final}")

#En caso de error :D
velocidad_final = velocidad_final
#PREGUNTA 3, 4 y 5

metros_vuelta = int(input())
vueltas = int(input())
vuelta = 1
total_circuito = metros_vuelta * vueltas
tiempo_total = 0
print(f"Inicio de la carrera de {nombre}")
print(f"Longitud de la pista: {metros_vuelta}")
mitad_carrera = total_circuito / 2

#Mantener velocidad original
velocidad_original = velocidad_final

#Estrella
star_activa = False
star_usadas = 0
seg_star_usadas = 0

metros_recorridos = 0
metros_recorridos_total = 0
print(f"Inicio de la vuelta {vuelta} / {vueltas}")



while metros_recorridos_total < total_circuito:
    
    #Ingreso de evento

    evento = input()

    if star_activa == True and seg_star_usadas < 5:
        if evento == "no hay evento":
            print(f"[ {metros_recorridos_total} m ] Avanzas con el poder de tu estrella!")
            seg_star_usadas +=1

        else:
            print(f"[ {metros_recorridos_total} m ] Te encontraste con el evento {evento}, pero no hace efecto porque viajas con el poder de la estrella!")
            seg_star_usadas +=1

        if seg_star_usadas == 5:
            seg_star_usadas = 0
            star_activa = False
        
        

    else:
        velocidad_final = velocidad_original

        if evento == "platano" and star_activa == False:
            print(f"[ {metros_recorridos_total} m ] Has resbalado con un platano! Tu velocidad se reduce al 25%")
            velocidad_final = velocidad_final / 4
        
        if evento == "agua" and star_activa == False:
            print(f"[ {metros_recorridos_total} m ] Te deslizaste por el agua! Tu velocidad se reduce al 50%")
            velocidad_final = velocidad_final / 2
          
        if evento == "caparazon" and star_activa == False:
            print(f"[ {metros_recorridos_total} m ] Chocaste con un caparazon! Tu velocidad se reduce a 0")
            velocidad_final = 0

        if evento == "no hay evento" and star_activa == False:
            print(f"[ {metros_recorridos_total} m ] Avanzas con normalidad")
            velocidad_final = velocidad_original

        if evento == "estrella":
            if star_usadas <2:
                star_activa = True
                star_usadas +=1
                print(f"[ {metros_recorridos_total} m ] Recogiste una estrella! Tu velocidad aumenta un 50% y no te afectan los otros eventos")
                velocidad_final = velocidad_final * 1.5
                seg_star_usadas+=1
            else:
                print(f"[ {metros_recorridos_total} m ] Te encontraste con una estrella, pero ya usaste el maximo permitido :(")
        

        #Incorporando
        if evento == "bala" and metros_recorridos_total >= mitad_carrera:
            velocidad_final = 0
            codigo = int(input())
            str_codigo = str(codigo)[1:3]
            metraje = int(str_codigo)
            metros_recorridos_total +=metraje
            print(f"[ {metros_recorridos_total} m ] Te has subido a la bala! Avanzaste {metraje} metros!")
            metros_recorridos += metraje
            metros_recorridos_total +=metraje
            
        elif evento == "bala" and metros_recorridos_total < mitad_carrera:
            print(f"[ {metros_recorridos_total} m ] Te encontraste con una bala antes de tiempo, avanzas a la velocidad normal")


    metros_recorridos += velocidad_final
    metros_recorridos_total += velocidad_final
    tiempo_total +=1


    if metros_recorridos > metros_vuelta:
        metros_recorridos -= metros_vuelta
        print(f"Has completado la vuelta {vuelta} / {vueltas} en {tiempo_total} segundos!")
        
        print(f"Llevas {metros_recorridos_total} / {total_circuito} metros recorridos")
        if vuelta < vueltas:
            vuelta+=1
            print(f"Inicio de la vuelta {vuelta} / {vueltas}")
        

print(f"¡Felicidades! {nombre} ha completado la carrera en {tiempo_total} segundos.")

#THIS VILLAVICENCIO NEVER LOSTt
#---------------------------------
