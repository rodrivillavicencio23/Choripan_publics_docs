"""
Ejemplo: en "el aire es azul" hay 3 palabras con vocal inicial: el, aire, es, azul = 4
"""
def cuenta_vocal_inicial(texto):
    if not texto:
        return 0
    lista_texto = texto.split(" ")
    palabras = filter(lambda x: list(x)[0] in ["a", "e", "i", "o", "u"],lista_texto)
    return len(list(palabras))

print(cuenta_vocal_inicial("el aire es azul"))   # 4
print(cuenta_vocal_inicial("hola amigo"))         # 1
print(cuenta_vocal_inicial(""))                   # 0


a = "hola"
print(list(a))