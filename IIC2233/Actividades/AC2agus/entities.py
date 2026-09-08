from collections import namedtuple

# Namedtupe que contiene 2 elementos: name (nombre de la persona) y
# award_name (nombre del premio)
Winner = namedtuple('Winner', ('name', 'award_name'))

class AwardStatistics:
    """
    Clase encargada de calcular estadisticas de ganadores de premios (awards)
    """

    def __init__(self):
        self.premios = []
        self.ganadores = []
        self.list_junta = []
        self.ganadores_unicos: set = set(self.ganadores)


    def add_winner(self, name: str, award_name: str) -> None:
        """
        Agrega un nuevo premio a las estadísticas, indicando el nombre del ganador, y el nombre del premio.
        """
        self.list_junta.append((name, award_name))
        if award_name not in self.premios:
            self.premios.append(award_name)
        if name not in self.ganadores:
            self.ganadores.append(name)

        return

    def get_top_winner(self) -> tuple[str, int]:
        artista_top = None
        cantidad = 0
        lista_unicos = []
        for artista in self.ganadores:
            if artista not in lista_unicos:
                lista_unicos.append(artista)  
        set_artistas = set(self.ganadores)
        for artis in set_artistas:
            cantidad_moment = 0
            for grup in self.list_junta:
                if artis == grup[0]:
                    cantidad_moment += 1
                    
            if cantidad_moment > cantidad:
                artista_top = artis
                cantidad = cantidad_moment     
        return (artista_top, cantidad)

    def get_top_winner_in_award(self, award_name: str) -> tuple[str, int]:
        set_unicos = (artista for artista in self.ganadores)
        dicc_unicos = {}
        
        for artista in set_unicos:
            for a in self.list_junta:
                if artista == a[0] and award_name == a[1]:
                    if artista not in dicc_unicos:
                        dicc_unicos[artista] = 1
                    else:
                        dicc_unicos[artista] += 1
        top = max(dicc_unicos, key=dicc_unicos.get)
        return top, dicc_unicos[top]
    
    
    def get_all_winners_in_award(self, award_name: str) -> set[str]:
        """
        Por completar: retorna un set con todos los ganadores del premio
        indicado (award_name)
        """
        set_retorno = set()
        for artista in self.ganadores:
            for general in self.list_junta:
                if artista == general[0] and general[1] == award_name:
                    set_retorno.add(artista)
        return set_retorno


    def get_egot_winners(self) -> set[str]:
        """
        Por completar: retorna un set con los nombres de las personas
        que han ganado un EGOT (Emmy, Grammy, Oscar, Tony)
        """
        ganadores_emmy = set()
        ganadores_grammy = set()
        ganadores_oscar = set()
        ganadores_tony = set()
        
        for artista in self.ganadores:
            for general in self.list_junta:
                if artista == general[0] and general[1] == "Emmy":
                    ganadores_emmy.add(artista)

                if artista == general[0] and general[1] == "Grammy":
                    ganadores_grammy.add(artista)

                if artista == general[0] and general[1] == "Oscar":
                    ganadores_oscar.add(artista)

                if artista == general[0] and general[1] == "Tony":
                    ganadores_tony.add(artista)

        set_retorno = ganadores_emmy & ganadores_grammy & ganadores_oscar & ganadores_tony
        # & = interesection : saca todos los valores que tengan en común (y solo esos)
        return set_retorno