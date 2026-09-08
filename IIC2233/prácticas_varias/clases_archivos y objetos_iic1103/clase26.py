#Objetos
class Gato:

    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return self.nombre+"("+str(self.edad)+")"

g1 = Gato("Garfield",10)
g2 = Gato("SiLVESTRE",5)
print(g1)

print(str(g2))

lista = [g1,g2]
for g in lista:
    print(g)
print(lista)