#Variables
menortiempo = 240000
mayortiempo = 0
ganador = 1
a = 1
seguir = True
#Def
def convertime (dife):
    hour = (dife //10000)*60*60
    minu = ((dife//100)%100)*60
    sec = (dife%100)
    total = hour + minu + sec
    #print(hour)
    #print(minu)
    #print(sec)
    print(f"o {total} segundos XD")


#Ciclo
players = int(input("Ingrese número de corredores: "))
while seguir:
    #Tiempo del primer lugar en secuencia
    menortiempo1= int(input(f"ingrese tiempo competidor {a}: "))
    if menortiempo1 < menortiempo:
        menortiempo = menortiempo1
        ganador = a
    #Tiempo del último lugar
    if menortiempo1 > mayortiempo:
         mayortiempo = menortiempo1
    #Romper ciclo cuando se llegue a la cantidad de corredores
    if a == players:
            seguir = False
    else:
        a+=1
dife = mayortiempo-menortiempo
print(f"Ganador: #{ganador}")
print(f"La diferencia con el último lugar fue de: {dife} (hh:mm:ss)")

convertime(dife)    
