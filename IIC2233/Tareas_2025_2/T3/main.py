# ------------------------------
import sys
from PyQt5.QtWidgets import QApplication
from frontend.ventana_inicial import VentanaIni
from frontend.ventana_principal import VentanaPri
from frontend.ventana_mapa import VentanaMapa
# ------------------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # ---- Crear ventanas ----
    ventana_inicial = VentanaIni()
    ventana_principal = VentanaPri()
    ventana_mapeo = VentanaMapa()
    # ---- Conexión de señales ----
    ventana_inicial.senal_abrir_menu.connect(lambda: ventana_principal.show())
    ventana_principal.senal_volver_inicio.connect(lambda: ventana_inicial.show())
    ventana_principal.senal_ir_mapeado.connect(lambda: ventana_mapeo.show())
    ventana_mapeo.senal_volver_menu.connect(lambda: ventana_principal.show())
    
    
    ventana_inicial.show()
    sys.exit(app.exec_())
    