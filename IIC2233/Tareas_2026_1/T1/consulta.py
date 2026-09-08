# -----------------------------------------------------------------------------
# Imports y modularización
from personajes import Estudiante, Ayudante, Profesor
from elementos import Arma, Habitacion
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Clase Consulta
# -----------------------------------------------------------------------------
class Consulta():
    def __init__(self, sospechoso_consultado: Estudiante | Ayudante | Profesor,
                arma_consultada: Arma, habitacion_consultada: Habitacion, 
                nombre_interrogado: str, habitacion_interrogacion: str):
        
        self.sospechoso_consultado = sospechoso_consultado
        self. arma_consultada = arma_consultada 
        self.habitacion_consultada = habitacion_consultada

        self.nombre_interrogado = nombre_interrogado
        self.habitacion_interrogacion = habitacion_interrogacion
        self.respuestas = []

        self.respuesta_sospechoso: str | None = None
        self.respuesta_arma: str | None = None
        self.respuesta_habitacion: str | None = None

    # -------------------------------------------------------------------------
    def agregar_respuesta(self, respuesta: str):
        self.respuestas.append(respuesta)
        return

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
