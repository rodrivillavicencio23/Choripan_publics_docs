
"""
Sets (Conjuntos) y sus métodos | ¿Para qué sirven los Sets en Python

definición: colecciones desordenadas de elementos/objetos únicos
- Mutables
"""

# Ejemplo de set
canasta: set = {"yoghurt", "leche", "piña", "atun", "ramitas", "leche"}

print(canasta)  # Imprimirá solamente los elementos únicos

# 2do ejemplo

numeros : set = {1, 2, 3, 5, 4, 2, 1, 4, 5, 6, 2, 10, 1, 2, 8} 

print(numeros)

# Añadir elemento a set
numeros.add(15)
print(numeros)


"""
Frozen sets: Inmutables (no se pueden agregar nuevos elementos)
"""
set_inmutable: frozenset = frozenset("DDog")

print(set_inmutable)
try:
    set_inmutable.add("hey brotha") # Va a arrojar error
except:
    print("Error, frozenset no tiene métodos de modificación")


# Métodos

# 1 - .intersecctiom
print(" \n ---------------- ")
conjunto_1 = {0,1,2,3,5,6}
conjunto_2 = {1,2,6,7,8}

conjunto_intersection = conjunto_1.intersection(conjunto_2)  # También se puede usar el ' & '

print(conjunto_intersection)    # {1, 2, 6}

# 2 - .union

conjunto_union = conjunto_1.union(conjunto_2)   # También se puede usar el ' | '
print(conjunto_union)   # {0, 1, 2, 3, 5, 6, 7, 8}

# 3 - .difference

conjunto_diferencia = conjunto_1.difference(conjunto_2)  # También se puede usar el ' - '
print(conjunto_diferencia)  # {0, 3, 5}

# 4 - .symmetric_difference : elementos únicos de cada conjunto

conjunto_diferencia_simetrica = conjunto_1.symmetric_difference(conjunto_2)

print(conjunto_diferencia_simetrica)    #{0, 3, 5, 7, 8}

# 5 - .issuperset : conjunto_1 contiene al conjunto_2, retorna valor Bool

conjunto_de_otro = conjunto_1.issuperset(conjunto_2)
print(conjunto_de_otro)     # False

con_1 = {1, 2, 3, 4}
con_2 = {1, 4}
con_de_otro = con_1.issuperset(con_2)

print(con_de_otro)  # True
