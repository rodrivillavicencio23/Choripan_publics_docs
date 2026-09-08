
class DCCpalooza:
    def __init__(self):
        pass

afinidad_min = 50
afinidad_max = 150


#|----- Clase Artista -----|
class Artista:
    """
    Clase para asignación de artistas luego de lectura de archivos .csv
    """
    def __init__(self,nombre, genero, dia, hit, afinidad_publico, afinidad_staff):
        self.nombre: str = nombre
        self.genero: str = genero
        self.dia: int = dia
        self.hit: str = hit
        self.afinidad_publico: int = afinidad_publico
        self.afinidad_staff: int = afinidad_staff

    @property
    def afinidad_con_publico(self):
        return self.afinidad_con_publico
    
    @afinidad_con_publico.setter
    def afinidad_con_publico(self, valor):
        if afinidad_min < valor < afinidad_max:
            self.afinidad_publico = valor
        else:
            if valor > 100:
                self.afinidad_publico = 100
            if valor < 0:
                self.afinidad_publico = 0

    @property
    def afinidad_con_staff(self):
        return self.afinidad_con_publico
    
    @afinidad_con_staff.setter
    def afinidad_con_staff(self, valor):
        if afinidad_min < valor < afinidad_max:
            self.afinidad_staff = valor
        else:
            if valor > 100:
                self.afinidad_staff = 100
            if valor < 0:
                self.afinidad_staff = 0
    
    @property
    def animo(self):
        return 0.5 * self.afinidad_publico + 0.5 * self.afinidad_staff




#|----- Clases con heredación (Pop, Xileno, Trap) -----|

class ArtistaPop(Artista):
    def __init__(self, *args, **kwargs): #---> ahorrarse aún más código
        super().__init__(*args, **kwargs)

class ArtistaChileno(Artista):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
