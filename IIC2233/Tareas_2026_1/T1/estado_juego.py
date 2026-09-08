# -----------------------------------------------------------------------------
# estado_juego.py
# -----------------------------------------------------------------------------
# Imports y modularización
from personajes import Sospechoso
from elementos import Arma, Habitacion
from consulta import Consulta
from cargar_datos import cargar_personajes, cargar_habitaciones, cargar_armas
from random import choice, shuffle
# -----------------------------------------------------------------------------

class EstadoJuego():
    def __init__(self):
        self.personajes: list[Sospechoso] = []
        self.habitaciones: list[Habitacion] = []
        self.armas: list[Arma] = []

        self.solucion_personaje: Sospechoso = None
        self.solucion_habitacion: Habitacion = None
        self.solucion_arma: Arma = None

        self.personaje_jugador: Sospechoso = None

        self.habitacion_actual: Habitacion = None
        self.rondas_jugadas = 0
        self.descartes = []
        self.no_descartados = []
        self.historial_consultas: list[Consulta] = []

    # -------------------------------------------------------------------------
    def cargar_datos(self):
        if not self.personajes:
            self.personajes = cargar_personajes()
            self.habitaciones = cargar_habitaciones()
            self.armas = cargar_armas()

    # -------------------------------------------------------------------------
    def elegir_asesino(self):
            if self.solucion_personaje is not None:
                return
            self.solucion_personaje = choice(self.personajes)
            self.solucion_habitacion = choice(self.habitaciones)
            self.solucion_arma = choice(self.armas)
    
    # -------------------------------------------------------------------------
    def elegir_personaje_jugador(self):
        if self.personaje_jugador is not None:
            return
        while self.personaje_jugador == None or \
            self.personaje_jugador == self.solucion_personaje:

            self.personaje_jugador = choice(self.personajes)
            return

    # -------------------------------------------------------------------------
    def asignar_sospechosos_a_habitaciones(self):
        habitaciones = self.habitaciones.copy()
        sospechosos = self.personajes.copy()

        shuffle(habitaciones)
        shuffle(sospechosos)

        for h in habitaciones:
            h.sospechoso = None

        while habitaciones and sospechosos:
            habitacion = habitaciones.pop()
            sospechoso = sospechosos.pop()

            habitacion.sospechoso = sospechoso
            sospechoso._ubicacion = habitacion

    # -------------------------------------------------------------------------
    def actualizar_lista_no_descartados(self):
        lista_limpia = []
        for sospechoso in self.personajes:
            if sospechoso not in self.descartes:
                lista_limpia.append(lista_limpia)
        self.no_descartados = lista_limpia

    # -------------------------------------------------------------------------
    def mostrar_lista_no_descartados(self):
        for num, sospechoso in enumerate(self.no_descartados):
            print(f"[{num}] : {sospechoso._nombre}")
            return



    # -------------------------------------------------------------------------
    def realizar_consulta(self, nombre_sospechoso: str, nombre_arma: str) -> Consulta | None:
        """
        Ejecuta una consulta al sospechoso en la habitación actual.
        La pregunta de habitación es siempre sobre la habitación actual.
        Retorna un objeto Consulta con las respuestas, o None si no
        hay sospechoso en la habitación actual.
        """
        persona_interrogada = self.obtener_sospechoso_habitacion_actual()
        if persona_interrogada is None:
            return None

        tipo_hab = self.habitacion_actual.tipo
        max_resp = persona_interrogada.max_respuestas(tipo_hab)

        consulta = Consulta(
            sospechoso_preguntado = nombre_sospechoso,
            arma_preguntada = nombre_arma,
            habitacion_preguntada = self.habitacion_actual.nombre,
            nombre_interrogado = persona_interrogada._nombre,
            habitacion_interrogacion = self.habitacion_actual.nombre)

        respuestas_dadas = 0

        # Pregunta sobre el sospechoso
        if respuestas_dadas < max_resp:
            resultado = persona_interrogada.responder(nombre_sospechoso)
            consulta.respuesta_sospechoso = resultado
            if resultado:
                self.descartes.append(resultado)
            respuestas_dadas += 1

        # Pregunta sobre el arma
        if respuestas_dadas < max_resp:
            resultado = persona_interrogada.responder(nombre_arma)
            consulta.respuesta_arma = resultado
            if resultado:
                self.descartes.append(resultado)
            respuestas_dadas += 1

        # Pregunta sobre la habitación actual
        if respuestas_dadas < max_resp:
            resultado = persona_interrogada.responder(self.habitacion_actual.nombre)
            consulta.respuesta_habitacion = resultado
            if resultado:
                self.descartes.append(resultado)

        self.historial_consultas.append(consulta)
        self.rondas_jugadas += 1
        return consulta

    # -------------------------------------------------------------------------
    def validar_acusacion(self, nombre_personaje, nombre_arma, nombre_habitacion):
            return (self.solucion_personaje._nombre == nombre_personaje
                and self.solucion_arma.nombre == nombre_arma
                and self.solucion_habitacion.nombre == nombre_habitacion)
    
    # -------------------------------------------------------------------------
    def obtener_sospechoso_habitacion_actual(self):
            if self.habitacion_actual is None:
                return None

            return self.habitacion_actual.sospechoso

    # -------------------------------------------------------------------------
    def verificar_pasaje_secreto(self):
        if self.habitacion_actual.pasadizo != "-":
            return True
        return False

    # -------------------------------------------------------------------------
    def usar_pasaje_secreto(self):
        origen = self.habitacion_actual
        destino_nombre = origen.pasadizo
        if not destino_nombre:
            return
        for hab in self.habitaciones:
            if hab.nombre == destino_nombre:
                self.habitacion_actual = hab
                return

    # -------------------------------------------------------------------------
    def mover_habitacion_indice(self, valor: int):
        indice = valor - 1
        self.habitacion_actual = self.habitaciones[indice]

    # -------------------------------------------------------------------------
    def obtener_habitacion_indice(self, valor: int):
        indice = valor - 1
        return self.habitaciones[indice].nombre
    
    # -------------------------------------------------------------------------
    def obtener_pasadizo_indice(self, valor: int):
        indice = valor - 1
        return self.habitaciones[indice].pasadizo
    
    # -------------------------------------------------------------------------
    def agregar_consulta_historial(self, consulta: Consulta):
         self.historial_consultas.append(consulta)
    
    

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
