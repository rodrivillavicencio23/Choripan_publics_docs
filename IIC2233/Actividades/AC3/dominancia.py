from bases import Gen, ParDeGenes
from abc import ABC, abstractmethod



class Dominante(Gen):
    """
    Clase que modela el comportamiento de genes dominantes
    """
    def __add__(self, other: Gen) -> ParDeGenes:
        """
        Por completar: Determina el fenotipo y retorna un ParDeGenes
        usando las reglas de dominancia

        """
        # Como este gen es dominante, su valor siempre define el fenotipo
        fenotipo = self.valor
        return ParDeGenes(self, other, fenotipo)



class Recesivo(Gen):
    """
    Clase que modela el comportamiento de genes recesivos
    
    """   
    def __add__(self, other: Gen) -> ParDeGenes:
        """
        Por completar: Determina el fenotipo y retorna un ParDeGenes
        usando las reglas de dominancia
        """
        if self.valor == other:
            fenotipo = self.valor
            return ParDeGenes(self, other, fenotipo)
        else:
            fenotipo = other.valor
            return ParDeGenes(self, other, fenotipo)
        pass

class Codominante(Gen):
    """
    Clase que modela el comportamiento de genes codominantes
    """
    def __add__(self, other: Gen) -> ParDeGenes:
        """
        Por completar: Determina el fenotipo y retorna un ParDeGenes
        usando las reglas de dominancia
        """
        fenotipo = None
        if isinstance(other, Dominante):
            fenotipo = other.valor
        elif isinstance(self, Dominante):
            fenotipo = self.valor
        elif self.valor == other.valor:
            fenotipo = self.valor
        else:
            fenotipo = f"Mezcla entre {self.valor} y {other.valor}"
        
        return ParDeGenes(self, other, fenotipo)
