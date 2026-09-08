from collections import namedtuple
"""
# Named Tuples: -> importar desde collections
estructuras que permiten definir campos para 
cada una de las posiciones en que han sido ingresados los datos. Son útiles como una forma de agrupar datos.
"""
Punto = namedtuple('Punto', ['x', 'y', 'lista_datos'])

punto_ejemplo = Punto(10, 20, [1, 2, 3])

print(punto_ejemplo)

print("\n -------  ")


#   ChileanRegister = namedtuple('ChileanRegister_type', ['RUT', 'name', 'age'])

PersonaFavorita = namedtuple('PersonaFavorita', ['nombre', 'apellido', 'edad', 'estatura', 'color_ojos', 'profesion'])
debraa = PersonaFavorita("Debra", "Palma", 22, 1.65, "Claros", "Modelo")
print(debraa, "\n")

# Imprimir por asignación de tuplas
print(f"{debraa.nombre} {debraa.apellido} tiene {debraa.edad} años, trabaja como: {debraa.profesion}, \n"
      f"mide {debraa.estatura}m y sus bellos ojos son {debraa.color_ojos}")

# Imprimir el elemento 5 de la namedtupla
print(debraa[5])

# Imprimir nombre de campos
print(debraa._fields)

# Obtener la tupla como diccionario
print("--- Tupla como dicc ---- \n")
print(debraa._asdict())



# 2do ejemplo
print("\n -------  ")

Tanque = namedtuple('Tanque','nombre anio penetracion blindaje')

tiger_ii = Tanque('Tiger II', 1944, 185, 180)

print(tiger_ii)


