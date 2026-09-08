# =============================================================================
# Imports y Modularización
import sys
from PyQt6.QtWidgets import QApplication
from frontend.ventana_inicial import VentanaIni
from frontend.ventana_indice import VentanaIndice
from frontend.ventana_simulacion import VentanaSimulacion
from backend.controlador import ControladorLogico
# =============================================================================

if __name__ == "__main__":

    app = QApplication(sys.argv)

    # ---- Crear ventanas ----
    ventana_inicial = VentanaIni()
    ventana_indice = VentanaIndice()
    ventana_simulacion = VentanaSimulacion()
    controlador_logico = ControladorLogico()
    # ---- Conexión de señales ----
    ventana_inicial.senal_abrir_indice.connect(lambda: ventana_indice.show())
    ventana_inicial.senal_abrir_simulacion.connect(lambda: ventana_simulacion.show())
    ventana_indice.senal_volver_inicio.connect(lambda: ventana_inicial.show())
    ventana_simulacion.senal_volver_inicio.connect(lambda: ventana_inicial.show())
    

    ventana_inicial.show()
    controlador_logico.empezar()
    sys.exit(app.exec())

# =============================================================================
# =============================================================================
# =============================================================================