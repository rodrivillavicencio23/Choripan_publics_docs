from random import randint

# Creamos el relleno
relleno = [1,2,3,4,5,6,3,2,3,5,3,2,3]

datos_limitrofes = (
    'El verdadero tesoro',
    *relleno, # Usamos el operador para rellenar nuestra tupla
    'son los amigos que hicimos en el camino'
)

# Vemos como quedo nuestra tupla
print(f'Tupla con informacion:', datos_limitrofes)

# Guardamos los datos de acuerdo a lo estipulado por el ejemplo
primer_elemento, *relleno, ultimo_elemento = datos_limitrofes

# Podemos ver que el relleno se almacena en una lista
print(f'Relleno almacenado:', relleno)
# Y podemos aplicar el mismo operador sobre dicha lista
# dentro de una funcion
print(f'Relleno desempaquetado:', *relleno)
# Imprimimos el mensaje oculto
print(f'Mensaje oculto: {primer_elemento} {ultimo_elemento}')