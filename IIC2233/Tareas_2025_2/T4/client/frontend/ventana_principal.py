# ------------------------------
# IMPORTS Y MODULARIZACIÓN
import os
import threading
from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QSizePolicy, QScrollArea,
    QHBoxLayout, QPushButton, QApplication, QMessageBox,
    QGroupBox)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, pyqtSignal, QEvent

# ------------------------------
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
# ------------------------------

# ------------------------------
# VENTANA PRINCIPAL
# ------------------------------
class VentanaPri(QWidget):
    senal_volver_inicio = pyqtSignal()
    senal_ir_blackjack = pyqtSignal()
    senal_ir_aviator = pyqtSignal()

    def __init__(self, connection, username, *args, **kwargs) -> None:
        """
        connection: instancia de ConnectionHandler / Cliente con send_text/recv_text/close
        username: nombre del usuario autenticado
        """
        super().__init__(*args, **kwargs)
        self.connection = connection
        self.username = username
        # estado local
        self._balance = None
        self.init_gui()
        self.setWindowTitle(f"DCCASINO: {self.username} - VENTANA PRINCIPAL")

        _install_event_handler(self.__class__)
        self.request_balance()

    def init_gui(self) -> None:
        self.setGeometry(720, 200, 1080, 720)

        # ---- IMAGEN DE FONDO ----
        self.fondo = QLabel(self)
        fondo_path = os.path.join("client", "frontend", "sprites", "background_images", "ventana_principal.png")
        pixmap = QPixmap(fondo_path) if os.path.exists(fondo_path) else QPixmap()
        self.fondo.setPixmap(pixmap)
        self.fondo.setScaledContents(True)

        # ---- ÍCONO DE LA VENTANA ----
        icon_path = os.path.join("client", "frontend", "background_images", "mono_icon.jpeg")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        # ---- LAYOUT PRINCIPAL VERTICAL ----
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)
        
        # ---------- IMAGEN DE TÍTULO ----------
        self.titulo_label = QLabel(self)
        self.titulo_label.setAlignment(Qt.AlignCenter)
        self.titulo_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        titulo_path = os.path.join("client", "frontend", "sprites", "background_images", "dcccasino.png")
        if os.path.exists(titulo_path):
            self.titulo_pixmap = QPixmap(titulo_path)
            self._actualizar_titulo()
        else:
            self.titulo_pixmap = None
            self.titulo_label.setText("DCCASINO")
            # Aplicamos estilo consistente
            self.titulo_label.setStyleSheet(
                "background-color: rgba(20,20,20,0.9); color: rgb(57,255, 20); "
                "font-size: 28px; padding: 8px; font-family: Constantia;"
            )

        main_layout.addWidget(self.titulo_label, alignment=Qt.AlignCenter)

        # ---------- INFO DEL USUARIO Y SALDO ----------
        info_layout = QHBoxLayout()
        self.user_label = QLabel(f"Usuario: << {self.username} >>")
        self.user_label.setStyleSheet(
            "background-color: rgba(20,20,20,0.9); color: rgb(57,255, 20); "
            "font-size: 18px; padding: 4px; font-family: Constantia;"
        )
        info_layout.addWidget(self.user_label)

        self.saldo_label = QLabel("Saldo: —")
        self.saldo_label.setStyleSheet(
            "background-color: rgba(20,20,20,0.9); color: rgb(57,255, 20); "
            "font-size: 18px; padding: 4px; font-family: Constantia;"
        )
        info_layout.addWidget(self.saldo_label)

        # ---- botón actualizar saldo manual ----
        btn_actualizar = QPushButton("Actualizar saldo")
        btn_actualizar.clicked.connect(self.request_balance)
        btn_actualizar.setFixedSize(180, 40)
        btn_actualizar.setStyleSheet(
            "background-color: rgba(20,20,20,0.9); color: rgb(57,255, 20); "
            "font-size: 18px; padding: 4px; font-family: Constantia;"
        )
        info_layout.addWidget(btn_actualizar)

        main_layout.addLayout(info_layout)

        # ---- botón volver inicio ----
        boton_volver = QPushButton("Volver inicio")
        boton_volver.clicked.connect(self.volver_inicio)
        boton_volver.setStyleSheet(
            "background-color: rgba(20,20,20,0.9); color: rgb(57,255, 20); "
            "font-size: 20px; padding: 6px; font-family: Constantia;"
        )
        main_layout.addWidget(boton_volver, alignment=Qt.AlignLeft)

        # ---------- BLOQUE DE BOTONES DE JUEGOS ----------
        botones = [
            ("Mesa de BlackJack💵♣️", self.ir_blackjack),
            ("AVIATOR 151✈️ ", self.ir_aviator),
            ("Ruleta 151🎰 \n (NO DISPONIBLE)", self.ir_ruleta)
        ]

        botones_layout = QHBoxLayout()
        for texto, accion in botones:
            btn = QPushButton(texto)
            btn.setFixedSize(300, 150)
            btn.setStyleSheet(
                "background-color: rgba(20,20,20,0.9); color: rgb(57,255, 20); "
                "font-size: 20px; padding: 6px; font-family: Constantia;"
            )
            btn.clicked.connect(accion)
            botones_layout.addWidget(btn)

        botones_layout.addStretch(0)
        main_layout.addLayout(botones_layout, 2)

        self.setLayout(main_layout)

    

    # ---------- ESCALADO DE FONDO ----------
    def resizeEvent(self, event):
        self.fondo.setGeometry(0, 0, self.width(), self.height())
        self._actualizar_titulo()
        super().resizeEvent(event)

    # ---------- IMAGEN DE TITULO AUTO - ESCALABLE ----------
    def _actualizar_titulo(self):
        if not hasattr(self, "titulo_pixmap") or not self.titulo_pixmap or self.titulo_pixmap.isNull():
            return
        ancho = int(self.width() * 0.5)
        alto = int(self.height() * 0.15)
        pixmap_scaled = self.titulo_pixmap.scaled(
            ancho, alto, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        self.titulo_label.setPixmap(pixmap_scaled)

    # ---------- ACCIONES ----------
    def volver_inicio(self):
        self.hide()
        self.senal_volver_inicio.emit()

    def ir_blackjack(self):
        self.hide()
        self.senal_ir_blackjack.emit()

    def ir_aviator(self):
        self.hide()
        self.senal_ir_aviator.emit()

    def ir_ruleta(self):
        QMessageBox.information(self, "Fuera de servicio", 
                                "Ruleta fuera de servicio (no implementado).")

    # ---------- SALDO ----------
    def request_balance(self):
        if not getattr(self, "connection", None):
            self._post_to_ui(lambda: QMessageBox.warning(self, "No conectado", "No hay conexión con el servidor."))
            return

        def worker():
            try:
                self.connection.send_text(f"GET_BALANCE {self.username}")
                resp = self.connection.recv_text()

                if not resp:
                    raise RuntimeError("Respuesta vacía del servidor.")

                parts = resp.strip().split()
                if parts[0].upper() == "BALANCE" and len(parts) >= 2:
                    amount = parts[1]
                    self._post_to_ui(lambda: self._update_balance_label(amount))
                else:
                    self._post_to_ui(lambda: QMessageBox.warning(self, "Respuesta inesperada", f"Resp: {resp}"))

            except ValueError as e:
                mensaje = str(e)
                print(mensaje)

        t = threading.Thread(target=worker, daemon=True)
        t.start()

    def _update_balance_label(self, amount):
        self._balance = amount
        self.saldo_label.setText(f"Saldo: {amount}")

    def _post_to_ui(self, fn):
        QApplication.instance().postEvent(self, _FuncEvent(fn))

    def closeEvent(self, event):
        super().closeEvent(event)


_install_event_handler(VentanaPri)
# ------------------------------
