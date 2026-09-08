

class perro():

    def __init__(self, nombre, raza, edad, color):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.color = color

    def __str__(self):
        return self.nombre+"("+str(self.edad)+")"



bobby = perro("Bobby","Pastor alemán",3,"blanco")
#bobby.ladrar()
#bobby.comer("comida de perros")
#bobby.correr(100)

print(bobby)


#   objeto.metodo(parámetros)
#            /\   ( constructor )
# los métodos se aplican sobre objetos

class Punto2D:
    def __init__(self):
        pass
