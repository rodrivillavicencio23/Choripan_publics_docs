# ------------------------------
# IMPORTS Y MODULARIZACIÓN
import sys
from PyQt5.QtWidgets import QApplication

from frontend.ventana_inicial import VentanaIni
from frontend.ventana_principal import VentanaPri
from frontend.ventana_aviator import VentanaAviator


class AppController:
    """
    Controlador central que mantiene referencias a las ventanas y gestiona
    la vida de la conexión y el flujo entre Inicio <-> Principal <-> Aviator.
    """
    def __init__(self, app: QApplication):
        self.app = app
        self.ventana_ini: VentanaIni | None = None
        self.ventana_pri: VentanaPri | None = None
        self.ventana_avi: VentanaAviator | None = None
        self.username: str | None = None

    def start(self):
        # Crear y mostrar ventana inicial
        self.ventana_ini = VentanaIni()
        # conectar señal de login
        self.ventana_ini.senal_conectado.connect(self.on_connected)
        self.ventana_ini.show()

    def on_connected(self, username: str):
        """
        Llamado cuando VentanaIni completó connect+handshake con éxito.
        Crea VentanaPri y realiza las conexiones de señales.
        """
        self.username = username
        conn = getattr(self.ventana_ini, "connection", None)

        # ---- si ya hay una ventana principal abierta por alguna razón, cerrarla limpiamente ----
        if self.ventana_pri:
            try:
                self.ventana_pri.close()
            except RuntimeError:  # ventana ya destruida
                pass
            self.ventana_pri = None

        # ---- cerrar ventana de aviator si sigue abierta ----
        if self.ventana_avi:
            try:
                self.ventana_avi.close()
            except RuntimeError:
                pass
            self.ventana_avi = None

        # crear la ventana principal con la conexión
        self.ventana_pri = VentanaPri(connection=conn, username=username)

        # conectar la señal de volver a una función del controlador
        self.ventana_pri.senal_volver_inicio.connect(self.handle_volver_inicio)

        # ocultar la inicial y mostrar la principal
        self.ventana_ini.hide()
        self.ventana_pri.show()

        # asegurar limpieza al salir de la app (si aún no se conectó)
        try:
            if not hasattr(self.app, "_cleanup_connected"):
                def cleanup_on_exit():
                    # intenta cerrar la conexión de la ventana principal si existe
                    try:
                        if self.ventana_pri and getattr(self.ventana_pri, "connection", None):
                            try:
                                self.ventana_pri.connection.close()
                            except (OSError, ConnectionError):
                                pass
                        elif self.ventana_ini and getattr(self.ventana_ini, "connection", None):
                            try:
                                self.ventana_ini.connection.close()
                            except (OSError, ConnectionError):
                                pass
                    except AttributeError:
                        pass
                self.app.aboutToQuit.connect(cleanup_on_exit)
                self.app._cleanup_connected = True
        except AttributeError:  # problema con atributo dinámico
            pass

    def handle_volver_inicio(self):
        """
        Se ejecuta cuando VentanaPri emite senal_volver_inicio.
        """
        if not self.ventana_pri:
            return

        # intentamos avisar al servidor (opcional; ignora errores)
        try:
            username = getattr(self, "username", None)
            if username and getattr(self.ventana_pri, "connection", None):
                try:
                    # Protocolo de ejemplo: LOGOUT <username>
                    self.ventana_pri.connection.send_text(f"LOGOUT {username}")
                except (BrokenPipeError, ConnectionResetError):
                    pass  # conexión caída
        except AttributeError:
            pass

        # cerrar y limpiar la conexión
        try:
            if getattr(self.ventana_pri, "connection", None):
                try:
                    self.ventana_pri.connection.close()
                except (OSError, ConnectionError):
                    pass
        except AttributeError:
            pass

        # desconectar señal para evitar duplicados en futuros ciclos
        try:
            self.ventana_pri.senal_volver_inicio.disconnect(self.handle_volver_inicio)
        except TypeError:  # señal no estaba conectada
            pass

        # cerrar ventana principal
        try:
            self.ventana_pri.close()
        except RuntimeError:  # ventana ya destruida
            pass
        finally:
            self.ventana_pri = None
            self.username = None

        # preparar ventana inicial: limpiar input y habilitar
        if self.ventana_ini:
            try:
                if hasattr(self.ventana_ini, "entrada"):
                    self.ventana_ini.entrada.setEnabled(True)
                    self.ventana_ini.entrada.clear()
                # aseguramos que no quede una conexión vieja
                self.ventana_ini.connection = None
            except AttributeError:
                pass
            # volver a mostrar la ventana inicial
            self.ventana_ini.show()


def main():
    app = QApplication(sys.argv)
    controller = AppController(app)
    controller.start()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
