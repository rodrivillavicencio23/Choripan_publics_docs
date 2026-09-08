# ------------------------------
# IMPORTS Y MODULARIZACIÓN

import os
import threading
from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton,
    QApplication, QLineEdit, QMessageBox, QProgressBar
)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, pyqtSignal
from backend.connection_handler import ConnectionHandler
# ------------------------------

# ------------------------------ 
class VentanaIni(QWidget):
    senal_conectado = pyqtSignal(str)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.connection = None
        self._connect_thread = None
        # atributos nuevos
        self.initial_balance = None
        self.is_new = False
        self.init_gui()
        self.setWindowTitle("DCCASINO: INICIO")
        self.show()

    def init_gui(self) -> None:
        self.setFixedSize(720, 480)

        # ---- BACKGROUND ----
        self.fondo = QLabel(self)
        fondo_path = os.path.join("client", "frontend", "sprites", "background_images", "ventana_inicial.png")
        pixmap = QPixmap(fondo_path) if os.path.exists(fondo_path) else QPixmap()
        self.fondo.setPixmap(pixmap)
        self.fondo.setScaledContents(True)
        self.fondo.setGeometry(0, 0, 720, 480)

        self.setWindowIcon(QIcon("client/frontend/sprites/background_images/mono_icon.jpeg"))

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(5)

        # ---- TÍTULO IMAGEN/TEXTO ----
        self.titulo_label = QLabel(self)
        titulo_path = os.path.join("client", "frontend", "sprites", "background_images", "dcccasino.png")
        if os.path.exists(titulo_path):
            self.titulo_label.setPixmap(QPixmap(titulo_path))
        else:
            self.titulo_label.setText("DCCASINO")
            self.titulo_label.setStyleSheet("color: rgb(57,255,20); font-size: 18px;")
        main_layout.addWidget(self.titulo_label, alignment=Qt.AlignCenter)
        main_layout.addStretch(1)

        #  ---- INPUT PARA NOMBRE DE USUARIO ----
        self.entrada = QLineEdit()
        self.entrada.setPlaceholderText("Ingrese su nombre de usuario")
        self.entrada.setStyleSheet(
            "background-color: black; color: rgb(200,255,10);"
            "border: 2px solid green; font-size: 18px; font-family: Times New Roman"
        )

        main_layout.addWidget(self.entrada, alignment=Qt.AlignCenter)

        # ---- LABEL BIENVENIDA ----
        self.info = QLabel("""
            <h1 style="color: rgb(57,255, 20); font-family: Segoe UI;">
                Bienvenido
            </h1>
        """)
        self.info.setAlignment(Qt.AlignCenter)
        self.info.setStyleSheet("color: white; font-size: 16px;")
        main_layout.addWidget(self.info)

        # ---- BARRA DE ESTADO ----
        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.status_label)

        # ---- BOTONES PRINCIPALES ----
        h_layout = QVBoxLayout()
        botones = [
            ("Ir al Menú Principal", self.btn_ir_menu_clicked),
            ("Abandonar GAMBLING", self.cerrar_programa),
        ]
        h_layout.addStretch(1)
        for texto, accion in botones:
            btn = QPushButton(texto)
            btn.setStyleSheet(
                "background-color: rgba(20,20,20,0.9); color: rgb(57,255,20); "
                "font-size: 22px; padding: 10px; font-family: Times New Roman;"
            )
            btn.clicked.connect(accion)
            h_layout.addWidget(btn)

        h_layout.addStretch(1)
        main_layout.addLayout(h_layout)

        self.setLayout(main_layout)

    # ---------- ACCIONES DE BOTONES ----------
    def btn_ir_menu_clicked(self):
        #---- VALIDACIÓN DE NOMBRE ----
        username = self.entrada.text().strip()
        if not username:
            QMessageBox.warning(self, "Nombre inválido", "Ingresa un nombre de usuario.")
            return
        # ---- DESACTIVAR INPUT Y MOSTRAR ESTADO ----
        self.entrada.setEnabled(False)
        self.status_label.setText("Conectando al servidor...")
        QApplication.processEvents()

        # ---- LANZAR THREAD QUE INTENTE CONECTAR Y HACER HANDSHAKE ----
        self._connect_thread = threading.Thread(target=self._connect_and_handshake, args=(username,), daemon=True)
        self._connect_thread.start()

    def _connect_and_handshake(self, username: str):
        if ConnectionHandler is None:
            self._on_connection_failed("Backend de conexión no disponible.")
            return

        ch = ConnectionHandler()
        ok = ch.connect()
        if not ok:
            self._on_connection_failed("No se pudo conectar al servidor.")
            return

        # ---- REALIZAR HANDSHAKE ----
        try:
            success = ch.handshake_and_auth(username)
        except Exception as e:
            ch.close()
            self._on_connection_failed(f"Error durante handshake: {e}")
            return

        if not success:
            ch.close()
            self._on_connection_failed("Nombre en uso o handshake rechazado.")
            return

        # ---- Si handshake OK, pedir saldo inmediatamente (en este mismo thread seguro) ----
        try:
            # enviar GET_BALANCE y leer respuesta
            ch.send_text(f"GET_BALANCE {username}")
            resp = ch.recv_text()
            if not resp:
                # si no hay respuesta, tratar como error
                ch.close()
                self._on_connection_failed("No se recibió respuesta de saldo del servidor.")
                return

            # parsear respuesta: puede ser "BALANCE <amount>" o "BALANCE <amount> NEW"
            tokens = resp.strip().split()
            if tokens[0].upper() != "BALANCE" or len(tokens) < 2:
                # respuesta inesperada
                ch.close()
                self._on_connection_failed(f"Respuesta inesperada al pedir saldo: {resp}")
                return

            # parse amount
            amount = tokens[1]
            # is_new flag si servidor envía tercer token "NEW"
            is_new = False
            if len(tokens) >= 3 and tokens[2].upper() == "NEW":
                is_new = True

            # guardar info en la instancia
            self.connection = ch
            self.initial_balance = amount
            self.is_new = is_new

            # informar en la UI (pasamos por _on_connection_success para ejecutar en hilo UI)
            self._on_connection_success(username)

        except Exception as e:
            ch.close()
            self._on_connection_failed(f"Error al solicitar saldo: {e}")
            return

    # ------ Métodos para actualizar UI (se llaman desde thread; usan Qt) ------
    def _on_connection_success(self, username: str):
        # este método puede ser llamado desde un hilo, así que usamos Qt to main loop
        def notify():
            # mostrar estado y saldo
            if getattr(self, "initial_balance", None) is not None:
                if getattr(self, "is_new", False):
                    QMessageBox.information(self, "Cuenta creada", f"Cuenta creada con saldo inicial: {self.initial_balance}")
                else:
                    QMessageBox.information(self, "Bienvenido de vuelta", f"Bienvenido {username}. Saldo: {self.initial_balance}")
                self.status_label.setText(f"Conectado ✅ | Saldo: {self.initial_balance}")
            else:
                self.status_label.setText("Conectado ✅")

            # ---- EMITIR SEÑAL CON EL USERNAME PARA QUE MAIN ABRA LA VENTANA PRINCIPAL ----
            self.senal_conectado.emit(username)

        QApplication.instance().postEvent(self, _FuncEvent(notify))

    def _on_connection_failed(self, reason: str):
        def notify():
            self.entrada.setEnabled(True)
            self.status_label.setText("")
            QMessageBox.critical(self, "Error de conexión", reason)
        QApplication.instance().postEvent(self, _FuncEvent(notify))

    def cerrar_programa(self):
        try:
            if self.connection:
                self.connection.close()
        except Exception:
            pass
        QApplication.instance().quit()


# ------------------------------
# Helpers para ejecutar funciones en hilo UI (mismo patrón que usas)
from PyQt5.QtCore import QEvent

class _FuncEvent(QEvent):
    EVENT_TYPE = QEvent.Type(QEvent.registerEventType())

    def __init__(self, fn):
        super().__init__(self.EVENT_TYPE)
        self.fn = fn


def _install_event_handler(widget_cls):
    orig_event = widget_cls.event
    def new_event(self, ev):
        if isinstance(ev, _FuncEvent):
            ev.fn()
            return True
        return orig_event(self, ev)
    widget_cls.event = new_event


_install_event_handler(VentanaIni)


# ----------------- prueba manual -----------------
if __name__ == "__main__":
    app = QApplication([])
    v = VentanaIni()
    def on_conn(name):
        print("Conectado como:", name)
        v.hide()
    v.senal_conectado.connect(on_conn)
    v.show()
    app.exec_()
