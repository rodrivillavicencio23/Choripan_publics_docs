vueltas = 4

vuelta = 1
long = 100
total_circuito = vueltas * long
velocidad = 40
recorrido = 0
recorrido_vuelta = 0
tiempo = 0
evento = ""
while recorrido < total_circuito:
    velocidad = 30
    evento = input()
    if evento == "f":
        velocidad = 40
        print(f"avanzas {velocidad} metros")
    elif evento == "d":
        velocidad = 20
        print(f"avanzas {velocidad} metros")

    recorrido += velocidad
    recorrido_vuelta += velocidad
    print("llevas de recorrido: ", recorrido)
    tiempo+=1
    if recorrido_vuelta >= long:
        print("llevas: ",recorrido)
        print(f"vuelta {vuelta} / {vueltas}")
        vuelta+=1
        recorrido_vuelta = 0

