# -----------------------------------------------------------------------------
# DCClue.py: módulo de estado y manejo del juego
# -----------------------------------------------------------------------------
# Imports y modularización

from estado_juego import EstadoJuego
# -----------------------------------------------------------------------------
# Clase manejadora/inicializadora del juego
class Dcclue():

    def __init__(self, nombre_jugador: str|None):
        self.nombre_jugador = nombre_jugador
        self.estado = EstadoJuego()

    # -------------------------------------------------------------------------
    def inicializar_estado(self):
        self.estado.cargar_datos()
        self.estado.elegir_asesino()
        self.estado.asignar_sospechosos_a_habitaciones()
        self.estado.elegir_personaje_jugador()



    # -------------------------------------------------------------------------
    def hacer_consulta(self, nombre_sospechoso: str, nombre_arma: str) -> str:
        consulta = self.estado.realizar_consulta(nombre_sospechoso, nombre_arma)
        if consulta is None:
            return "No hay sospechoso en esta habitación."
        return str(consulta)

    # -------------------------------------------------------------------------
    def turno_efectuado(self):
        self.estado.asignar_sospechosos_a_habitaciones()
    
    # -------------------------------------------------------------------------
    def mostrar_opciones_no_descartadas(self):
        for num, sospechoso in enumerate(self.estado.personajes):
            if sospechoso not in self.estado.descartes:
                print(num)

    # -------------------------------------------------------------------------
    def datos_asesino(self):
        return f"{self.estado.solucion_personaje._nombre
               } | {self.estado.solucion_habitacion.nombre
                } | {self.estado.solucion_arma.nombre}"
    
    # -------------------------------------------------------------------------
    def __str__(self):
        return f"Partida de: {self.nombre_jugador}"
    
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------