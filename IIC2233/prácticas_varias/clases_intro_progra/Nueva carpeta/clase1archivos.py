nombre_archivo = input("ARCHIVO PARA CONTAR LINEAS?: ")


#Abrir archivos open("{archivo}")
#open(nombre_archivo)

arch = open(nombre_archivo,"w")
print("hola",file=arch)
arch.close()
#para leer listas con el siguiente formato: 
lista = arch.readlines()
print(lista)