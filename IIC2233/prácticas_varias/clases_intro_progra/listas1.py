#APUNTES DE LISTA

#DEFINIR LISTA
lista  = ["O. Marsella","Liverpool","Bayern","AC Milán","Real Madrid"]

#LARGO LISTA: len(lista)
largo_lista = len(lista)
print("El más grande de ALEMANIA")

#Printear x elemento de la lista: print(lista[x])
print(lista[2])
print("!!!!!!!!!!!!!!!!!!!!!!!")

#Mostrando todos los elementos de la lista
for a in range(0,largo_lista):
    print(lista[a])

#Agregar elemento a la lista (quedará en la última posición) : lista.append(elemento)
lista.append("Ajax")
print(lista)

#Agregar elemento en x posición de la lista: lista.insert(x,elemento)
lista.insert(1,"Benfica")
print(lista)

#Elimina la primera aparición del elemento x en la lista. Lanza un error si el elemento no está en la lista: lista.remove(elemento)
lista.remove("AC Milán")
print(lista)

#Elimina y devuelve el elemento en la posición i. Si i no se proporciona, elimina y devuelve el último elemento de la lista.

equipo = lista.pop(4)
ultimo_equipo = lista.pop()
print(equipo)
print(ultimo_equipo)

#Reemplazar elemento de la lista en x indice: lista[x] = elemento

lista[0] = "PSG"
print(lista)

#Sumar listas: nuevalista = lista + lista2

lista2 = ["Gremio","Boca Juniors","Colo Colo","Deportes Táchira","Alianza Lima","Liga de Quíto","Atlético Nacional","Bolívar","Olimpia","Peñarol"]

equipos = lista+lista2
print(equipos)

#join
