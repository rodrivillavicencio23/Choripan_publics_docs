# =============================================================================
# Imports y Modularización
from PyQt6.QtCore import QObject, pyqtSignal
from backend.consultas import cargar_juguete
# =============================================================================



class ControladorLogico(QObject):

    senal_1 = pyqtSignal(int)

    def __init__(self) -> None:
        super().__init__()

    def empezar(self):
        pass

    def mostrar_juguetes(self):
        info_juguetes = cargar_juguete("data/juguetes.csv")
        for juguete in info_juguetes:
            yield (juguete.id_juguete, juguete.nombre, juguete.sprite)

# =============================================================================
# =============================================================================
# =============================================================================s
