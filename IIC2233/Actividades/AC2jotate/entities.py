from collections import namedtuple

# Namedtupe que contiene 2 elementos: name (nombre de la persona) y
# award_name (nombre del premio)
Winner = namedtuple('Winner', ('name', 'award_name'))

class AwardStatistics:
    """
    Clase encargada de calcular estadisticas de ganadores de premios (awards)
    """

    def __init__(self):
        self.diccionario_ganadores = {}#comienza estando vacio debido a que aun no se agregan ganadores
        self.todos_los_ganadores = []
        self.todos_los_premios = []

    def add_winner(self, name: str, award_name: str) -> None:
        self.name = str(name)
        self.award_name = str(award_name)
        self.diccionario_ganadores[name] = award_name

    def get_top_winner(self) -> tuple[str, int]:
        nombre = None  # "" --> None
        cantidad_premios = 0
        unicos = set(a for a in self.diccionario_ganadores.keys())
        for i in unicos:
            contador = 0
            for j in self.diccionario_ganadores.keys():
                #print(i, j)
                if i == j:
                    contador += 1
            if contador > cantidad_premios:
                cantidad_premios = contador
                nombre = i
        tupla = (nombre, cantidad_premios)
        return tupla
                

    def get_top_winner_in_award(self, award_name: str) -> tuple[str, int]:
        self.award_name = str(award_name)
        nombre = ""
        cantidad_premios = 0
        for i, j in self.diccionario_ganadores.items():
            contador = 0
            for k,z in self.diccionario_ganadores.items():
                if i == k and j == z and  j == award_name:
                    contador +=1
            if contador > cantidad_premios:
                cantidad_premios = contador
                nombre = i
        tupla = (nombre,cantidad_premios)
        return tupla
    
    def get_all_winners_in_award(self, award_name: str) -> set[str]:
        self.award_name = str(award_name) 
        # ??? Para que creaste esta variable?
        # ya te lo pasan como string
        for m, v in self.diccionario_ganadores.items():
            if v == award_name:
                # acá solo evaluas si el premio es igual, pero nunca validas si es el mismo artista
                self.todos_los_ganadores.append(m)
                # Te piden retornar un set, no una lista
        return self.todos_los_ganadores

    def get_egot_winners(self) -> set[str]:
        for m,a in self.diccionario_ganadores.items():    
            contador = 0
            for j,k in self.diccionario_ganadores.items():
                print(j, k) # PRINT AÑADIDO
                if m == j and k == "Emmy":
                    contador +=1
                if m == j and k == "Oscar":
                    contador +=1
                if m == j and k == "Grammy":
                    contador +=1
                if m == j and k == "Tony":
                    contador +=1
                #print(contador) #PRINT AÑADIDO
            if contador >= 4:
                self.todos_los_premios.append(m)
        return self.todos_los_ganadores