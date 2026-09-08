

archivo = open('sudamerica.txt')
lista = archivo.readlines()

print(lista)

print("Numero de lineas :"+str(len(lista)))


archivo.close() #No necesario pero es buena practica

"""Errores comunes
• f = open(“archivo_que_no_existe.txt”) à IOError No
such file
• f = open(“directorio”) à IOError Is a Directory"""