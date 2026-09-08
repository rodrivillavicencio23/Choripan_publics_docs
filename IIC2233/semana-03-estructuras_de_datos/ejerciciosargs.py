from collections import namedtuple

def suma(x,y,z):
    try:
        suma = x+y+z
        return suma
    except TypeError:
        raise("TypeError: se han entregado más parámetros de los indicados")
lista = [1,2,3]

# args
print(suma(*lista))

# lista_2 = [1,2,3,4]
# print(suma(*lista_2))    # Error: se toman 3 argumentos pero se reciben 4


# Kwargs



print("\n ---- kwargs ---- \n")
print("ej1:")
print(suma(x = 10, y = 20, z = -30))

def imprimir_dicc(nombre, apellido, edad, estatura, color_ojos, profesion):
    print(f"Nombre: \t {nombre}\n"
          f"Apellido: \t {apellido}\n"
          f"edad: \t {edad}\n"
          f"estatura: \t {estatura}\n"
          f"color de ojos: \t {color_ojos}\n"
          f"profesion: \t {profesion}\n")
    return
    

PersonaFavorita = namedtuple('PersonaFavorita', ['nombre', 'apellido', 'edad', 'estatura', 'color_ojos', 'profesion'])
debraa = PersonaFavorita("Debra", "Palma", 22, 1.65, "Claros", "Modelo")

dicc_debra: dict = debraa._asdict()
print(dicc_debra)
imprimir_dicc(**dicc_debra)