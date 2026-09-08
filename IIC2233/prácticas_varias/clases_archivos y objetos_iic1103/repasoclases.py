class Gato:
    def __init__(self, nombre, edad, color, estado):
        self.nombre = nombre
        self.edad = int(edad)
        self.color = color
        self.estado = estado

    def maullar(self):
        if self.estado.lower() == "sano":
            return "Miauu"
        elif self.estado.lower() == "enfermo":
            return "Meoww...."
        else:
            return "El gato no se siente bien para maullar."
        
    def __str__(self):
        return self.nombre+"-"+str(self.edad)


class Perro:
    def __init__(self, nombre, edad, raza, estado):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.estado = estado

    def ladrar(self):
        if self.estado.lower() == "sano":
            return "Guau Guau!"
        elif self.estado.lower() == "enfermo":
            return "Guu... guau..."
        else:
            return "El perro no tiene fuerzas para ladrar."
    def __str__(self):
        return self.nombre+"-"+self.edad


# Ejemplos de uso:
def criterio(item): 
    return item.edad


perro1 = Perro("Pepo", 4, "Quiltro", "sano")
perro2 = Perro("Roco", 6, "Bulldog", "enfermo")

print(perro1.ladrar()) 
print(perro2.ladrar())  

lista = []



gato1 = Gato("Pupi", 6, "naranja", "sano")
gato2 = Gato("Destructor de mundos", 5, "blanco", "enfermo")
gato3= Gato("xd",12,"rojo","sano")

lista = [gato1,gato2,gato3]
print(lista)
lista.sort(key=criterio)
for i in range(len(lista)):
    print(lista[i])

