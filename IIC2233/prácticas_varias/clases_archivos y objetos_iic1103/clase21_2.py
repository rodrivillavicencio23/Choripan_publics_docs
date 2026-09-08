import random
def palabra_azar():
    arch = open("paises.txt",encoding="latin-1")
    lineas = arch.readlines()
    n = len(lineas)
    azar = random.randint(0,n-1)
    arch.close()
    return lineas[azar].strip()

for i in range(10):
    print(palabra_azar())

#➕ Agregar sin borrar (modo append)
a = open("sudamerica.txt","a")

print("Guyana Francesa", file=a)
a.close()

a = open("sudamerica.txt","a")
for b in range(5):
    print("Guyana Francesa", file=a)

a.close()




#📖 Leer un archivo

"""archivo = open('archivo.txt', 'r')  # abrir en modo lectura
lineas = archivo.readlines()       # guardar las líneas como lista
archivo.close()                    # cerrar el archivo (buena práctica)
Cada línea termina con \n → usa .strip() para eliminarlo al imprimir.

Si el archivo no existe → lanza IOError."""



#✍️ Escribir en un archivo

"""archivo = open('archivo.txt', 'w')  # modo escritura: borra el contenido
print("texto a guardar", file=archivo)
archivo.close()
print(..., file=archivo) escribe en el archivo (añade \n por defecto).

Si el archivo ya existe, se sobrescribe."""



#➕ Agregar sin borrar (modo append)

"""archivo = open('archivo.txt', 'a')  # modo agregar
print("otra línea", file=archivo)
archivo.close()"""


#🧠 Conceptos clave
"""'r': leer

'w': escribir (sobrescribe)

'a': agregar al final

Siempre cierra el archivo después de usarlo.

Los archivos .csv son texto plano con valores separados por comas o punto y coma (Excel)."""