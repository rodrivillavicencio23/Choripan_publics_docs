# -----------------------------------------------------------------------------
# Imports y modularización
# NADA
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Clase Habitación
# -----------------------------------------------------------------------------
class Habitacion:
    def __init__(self, nombre: str, tipo: str, pasadizo: str):
        self.nombre = nombre
        self.tipo = tipo
        self.pasadizo = pasadizo
        self.sospechoso  = None
    
    # -------------------------------------------------------------------------
    def hay_sospechoso(self) -> bool:
            return self.sospechoso is not None

    # -------------------------------------------------------------------------
    def guardar(self):
        return f"{self.nombre},{self.tipo},{self.pasadizo}"
    def __str__(self):
        return f"{self.nombre} | {self.tipo} | {self.pasadizo} |"
    
# -----------------------------------------------------------------------------
# Clase Arma
# -----------------------------------------------------------------------------
class Arma():
    def __init__(self, nombre: str, tipo: str):
        self.nombre = nombre
        self.tipo = tipo

    # -------------------------------------------------------------------------
    def guardar(self):
        return f"{self.nombre},{self.tipo}"
    def __str__(self):
        return f"{self.nombre} | {self.tipo} |"
    
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
    

