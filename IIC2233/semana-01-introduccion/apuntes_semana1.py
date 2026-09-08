# -------------------------------------------------
# Apuntes semana 1: Introducción
# -------------------------------------------------

# Tipos de Datos en general (Aprendido)

# Funciones

# Importación y modularización
# --- Aliasing ---
"""
Se puede dar el nombre que uno quiera al módulo que
estamos importando junto a sus funciones
ej:

Import modulo as alias

alias.funcion_1(parametro_1, parametro_2, ...,)

"""

# --- Archivos ---

"""
open(path, modo): se debe definir para una variable para
así representar el archivo en path. El parámetro -modo-
indica como abrir el archivo:

'r' = Lectura (por defecto)
'w' = Escritura
'a' = Append

file.close() : cierra el archivo.

file.readline() : Retorna la línea siguiente
del archivo.

file.readlines() : retorna una variable del tipo
lista de todo el contenido del archivo.

--- Crear archivos ---

file.write(s) : escribe el string 's' en el archivo
(no agrega el caracterde fin de línea '\n')

print(s, file = file) : escribe el string 's' en el 
archivo (sí agrega el '\n').


"""

# --- Objetos (APRENDIDO)

# -.- Más sobre string -.-
"""String: secuencia inmutable de caracteres
Unicode (un string no es modificable). Se tiene
que crear un nuevo string oo sobreescribir el que
tenemos para poder modificarlo
Ejemplo de string:
"""
cadena = "mi cadena de texto"
print(cadena[0], cadena[-1])
"""

Ejemplo de mal uso de strings:

cadena = [0] = "M"

Ejemplo de buen uso de string:

cadena = "Mi nueva cadena de texto:

print(cadena)

"""
# --- Formas de crear un string en Python:
a = "programando"
b = 'mucho'
c = '''un string
con múltiples
lineas'''
d = """Multiples con
     comillas dobles"""
e = ("Tres" " strings" " juntos")
f = "un string " + "concatenado"
g = ("Otra forma de string que nos permite "
     "utilizar más de una línea pero en verdad solo es una,"
     " lo que es muy útil para cumplir PEP-8 :)")

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

# --- Secuencia de escape --- 
"""El \ se denomina carácter de escaoe
y se combina con otros carácteres ya ocupados
para python y que no se pueden escribir como tal
en la terminal a menos que se complemente con este:

\"   : Comilla doble
\'   : Comilla simple
\n   : Salto de linea
\t   : TAB (salto de línea)
\\   : Barra inversa o backslash

"""
frase = ("Debra Palma, eres la mujer más \'hermosa\' \n"
         "que mi alma a presenciado en este mundo \t <3")
print("\n--- Secuencia de escape --- ")
print(frase)

# --- Métodos disponiles en Strings ---
"""
La clase `str` tiene muchos métodos para manipular
"""
print(dir(str))
"""
# --- Métodos de strings de validación:

- str.isdigit() : ¿Está compuesto solo por dígitos?
- str.endswith(s) : ¿Termina con este otro _string_ `s`?
- str.index(s) : ¿En qué posición empieza este otro? 
- str.find(s) : ¿En qué posición empieza este string? (sin índice)

# --- Métodos de modificación de Strings:

- str.split("") : Retorna una lista de strings a partir de 
                separar el original en lo que colocamos en 
                las comillas

-"".join(lista) : Concatena todos los elementos de la secuencia
                dada por medio de un string ( "" )

- string.replace(" ", "##") :Entrega un nuevo string en que 
                            se reemplazó cada " " por "**".

                        
"""


