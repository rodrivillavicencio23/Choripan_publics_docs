# ------------------------------
# Imports y Modularización
import os
from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QSizePolicy,
                            QHBoxLayout, QPushButton, QApplication, QScrollArea)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, pyqtSignal
# ------------------------------

# ------------------------------
# Ventana Mapeado 
# ------------------------------
class VentanaMapa(QWidget):
    senal_volver_menu = pyqtSignal()
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.init_gui()
        self.setWindowTitle("DCCOSMOS: MAPA ESTELAR")

    def init_gui(self) -> None:
        self.planetas = ("criogenico",
                         "gas",
                         "liquido",
                         "plasma",
                         "rocoso")

        self.setGeometry(720, 200, 1080, 720)

        # ---- IMAGEN DE FONDO ----
        self.fondo = QLabel(self)
        fondo_path = os.path.join("frontend", "sprites", "fondo_mapa.png")
        pixmap = QPixmap(fondo_path)
        self.fondo.setPixmap(pixmap)
        self.fondo.setScaledContents(True)

        # ---- ÍCONO DE VENTANA ----
        self.setWindowIcon(QIcon("frontend/sprites/mono.jpg"))

        # ---- LAYOUT PRINCIPAL VERTICAL ----
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        # ---------- IMAGEN DE TÍTULO ----------
        self.titulo_label = QLabel(self)
        self.titulo_label.setAlignment(Qt.AlignCenter)
        self.titulo_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        titulo_path = os.path.join("frontend", "sprites", "dccosmos_mapa.png")
        if os.path.exists(titulo_path):
            self.titulo_pixmap = QPixmap(titulo_path)
            self._actualizar_titulo()
        else:
            self.titulo_pixmap = None
            self.titulo_label.setText("DCCOSMOS: CONSULTAS MENACE")
            self.titulo_label.setStyleSheet("color: white; font-size: 18px;")

        main_layout.addWidget(self.titulo_label, alignment=Qt.AlignCenter)
        
        # ---------- FILA DE BOTONES ----------
        h_layout = QVBoxLayout()
        botones = [
            ("Volver al Menú Principal", self.volver_inicio)
        ]
        h_layout.addStretch(1)  # centrado
        for texto, accion in botones:
            btn = QPushButton(texto)
            btn.setStyleSheet(
                "background-color: rgba(20,20,20,0.9); color: yellow; "
                "font-size: 20px; padding: 10px;"
            )
            btn.clicked.connect(accion)
            main_layout.addWidget(btn)
        h_layout.addStretch(1)
        main_layout.addLayout(h_layout)
        self.setLayout(main_layout)

    # ---------- ESCALADO DE FONDO ----------
    def resizeEvent(self, event):
        self.fondo.setGeometry(0, 0, self.width(), self.height())
        self._actualizar_titulo()
        super().resizeEvent(event)

    # ---------- IMAGEN DE TITULO AUTO - ESCALABLE ----------
    def _actualizar_titulo(self):
        if not self.titulo_pixmap or self.titulo_pixmap.isNull():
            return
        ancho = int(self.width() * 0.5)  
        alto = int(self.height() * 0.15) 
        pixmap_scaled = self.titulo_pixmap.scaled(
            ancho, alto, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        self.titulo_label.setPixmap(pixmap_scaled)

    # ---------- ACCIONES DE BOTÓN ----------
    def volver_inicio(self):
        self.hide()
        self.senal_volver_menu.emit()