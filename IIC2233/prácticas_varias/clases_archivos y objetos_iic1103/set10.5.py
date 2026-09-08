class Gato:
    def __init__(self, nombre, color, peso, edad,ultima_vacuna):
        self.nombre = nombre
        self.color = color
        self.peso = peso
        self.edad = edad
        self.ultima_vacuna = ultima_vacuna

    def __str__(self):
        return (f"{self.nombre} de color {self.color}")
def criterio(item):
    return item.peso


garf = Gato("Garfield", "Naranjo", 100, 10, 2017)
tom = Gato("Tom", "Gris", 5, 15, 2018)
silv = Gato("Silvestre", "Blanco y negro", 8, 12, 2015)
bot = Gato("Gato con Botas", "Naranjo", 4, 10, 2019)
grump = Gato("Grumpy Cat", "Gris", 8, 10, 2019)

gatos = [garf, tom, silv, bot, grump]
gatos_ordenados =sorted(gatos,key=criterio,reverse=True)

for a in gatos_ordenados:
    print(a)