def obtener_puntaje(palabra):
    puntos = 0
    for d in palabra:
        if d in "aeiouAEIOU":
            puntos +=3
        elif d.isnumeric():
            puntos +=int(d)
        elif d not in "AEIOUaeiou":
            puntos+=1
    return puntos

xd = "543"

print(obtener_puntaje(xd))