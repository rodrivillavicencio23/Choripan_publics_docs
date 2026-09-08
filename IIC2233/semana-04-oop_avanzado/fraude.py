
#|-----------------------------------|
#Herencia en OOP
#|-----------------------------------|

#atributos de instancia: instancia en particular de cada clase, hechos para solamente esa instancia pueda acceder a ellos
#atributos de clase: atributos que se ponen antes del init

#¿Qué significa heredar en OOP?

#significa que yo tengo una clase, y luego una nueva, hago que esta nueva clase herede los atributos de la 1ra clase, 
#reciclando código

#NO hay límite para heredar 




class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print("Wena socio")


class Farsante(Persona):
    def __init__(self,nombre,estafar: bool):
        super().__init__(nombre)
        self.estafar = estafar

    def saludar(self):
        print("te han saludado brutalmente")

    def super_estafa(self):
        if self.estafar:
            print(f"haz sido estafado por {self.nombre}")
            print(
                    """
                    ⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀⠀⠀⠀
                    ⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
                    ⠀⠀⠀⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇⠀
                    ⠀⠀⢤⣀⣀⣀⠀⠀⢸⣷⡄⠀⣁⣀⣤⣴⣿⣿⣿⣆
                    ⠀⠀⠀⠀⠹⠏⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠴⢿⢿⣿⡿⠷⠀⣿⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃⠀
                    ⠀⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟⠁

                    """)
        else:
            print("te haz salvado wacho")

persona_1 = Farsante("Socio", True)
persona_1.super_estafa()

persona_1.saludar()
#|-----------------------------------|
#Polimorfismo
#|-----------------------------------|

#Actuar de distintas maneras según las clases

#Overloading no existe en python

#|-----------------------------------|
#Multiherencia
#|-----------------------------------|

#Herencia múltiple permite heredar más de una clase


#|-----------------------------------|
#Clases abstractas
#|-----------------------------------|

#"COSAS DISEÑADAS DE UN PROGRAMADOR PARA OTRO PROGRAMADOR, PERO QUE M----"

#Restricciones para instanciar ciertos atributos en clases

#|-----------------------------------|
#Decoradores
#|-----------------------------------|

