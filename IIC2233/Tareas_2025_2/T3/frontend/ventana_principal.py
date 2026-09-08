# ------------------------------
# Imports y Modularización
import os
from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QSizePolicy,
                            QHBoxLayout, QPushButton, QApplication,
                            QScrollArea, QFileDialog, QSlider, QGroupBox, 
                            QLineEdit)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, pyqtSignal
# ------------------------------

# ------------------------------
# Ventana Principal 
# ------------------------------
class VentanaPri(QWidget):
    senal_volver_inicio = pyqtSignal()
    senal_ir_mapeado = pyqtSignal()

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.init_gui()
        self.setWindowTitle("DCCOSMOS: PANTALLA PRINCIPAL")

    def init_gui(self) -> None:
        self.setGeometry(720, 200, 1080, 720)

        # ---- IMAGEN DE FONDO ----
        self.fondo = QLabel(self)
        fondo_path = os.path.join("frontend", "sprites", "gato_planeta.png")
        pixmap = QPixmap(fondo_path)
        self.fondo.setPixmap(pixmap)
        self.fondo.setScaledContents(True)

        # ---- Ícono de la ventana ----
        self.setWindowIcon(QIcon("frontend/sprites/mono.jpg"))

        # ---- LAYOUT PRINCIPAL VERTICAL ----
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # ---------- IMAGEN DE TÍTULO ----------
        self.titulo_label = QLabel(self)
        self.titulo_label.setAlignment(Qt.AlignCenter)
        self.titulo_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        titulo_path = os.path.join("frontend", "sprites", "dccosmos_consultas.png")
        if os.path.exists(titulo_path):
            self.titulo_pixmap = QPixmap(titulo_path)
            self._actualizar_titulo()
        else:
            self.titulo_pixmap = None
            self.titulo_label.setText("DCCOSMOS: CONSULTAS MENACE")
            self.titulo_label.setStyleSheet("color: white; font-size: 18px;")

        main_layout.addWidget(self.titulo_label, alignment=Qt.AlignCenter)
        
        # ---------- BLOQUE DE BOTONES ----------
        self.archivo_proceso = None
        mensaje = self.archivo_proceso if self.archivo_proceso else "(Sin archivo cargado)"
        
        botones = [
            ("Volver Inicio", self.volver_inicio),
            ("Mapa Estelar", self.ir_mapeado),
            ("Abrir archivo CSV", self.abrir_archivo),
            (f"Realizar consulta", self.hacer_consulta)
        ]

        botones_layout = QVBoxLayout()
        botones_layout.addStretch(1)
        for texto, accion in botones:
            btn = QPushButton(texto)
            btn.setFixedSize(325,40)
            btn.setStyleSheet(
                "background-color: rgba(20,20,20,0.9); color: yellow; "
                "font-size: 12px; padding: 2px;"
            )
            btn.clicked.connect(accion)
            btn.setFixedSize(220, 50)
            botones_layout.addWidget(btn)
        

        # ---- ENTRADA DE TEXTO PARA FILTRO ----
        self.entrada_filtro = QLineEdit(self)
        self.entrada_filtro.setStyleSheet("background-color: rgba(20,20,20, 0.9);" \
        "color: yellow; font-size: 12px")
        botones_layout.addWidget(self.entrada_filtro)

        self.texto_entrada_filtro = self.entrada_filtro.text()
        
        botones_layout.addStretch(1)
        main_layout.addLayout(botones_layout)

        # ---------- SCROLL DE LISTA ----------
        scroll_group = QGroupBox("Resultados Consulta: ")
        scroll_group.setStyleSheet("color: white;" \
        "background-color: rgba(255,255,255,0.1)")
        scroll_layout = QVBoxLayout(scroll_group)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        contenedor = QWidget()
        vbox_scroll = QVBoxLayout(contenedor)
        for i in range(50):
            vbox_scroll.addWidget(QLabel(f"ERROR: NO IMPLEMENTADO #{i}"))
        scroll_area.setWidget(contenedor)
        scroll_layout.addWidget(scroll_area)

        main_layout.addWidget(scroll_group)

    

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

    # ---------- ACCIONES ----------
    def volver_inicio(self):
        self.hide()
        self.senal_volver_inicio.emit()

    def ir_mapeado(self):
        self.hide()
        self.senal_ir_mapeado.emit()

    def abrir_archivo(self):
        opciones = QFileDialog.Options()
        ruta_archivo, _ = QFileDialog.getOpenFileName(self,
            "Seleccionar archivo CSV",
            "",
            "Archivos CSV (*.csv)",
            options=opciones)
        if ruta_archivo:
            self.archivo_proceso = ruta_archivo
            print(f"Archivo seleccionado: {ruta_archivo}")
        else:
            print("No se seleccionó ningún archivo.")

    def hacer_consulta(self):
        print(self.entrada_filtro.text())
        self.entrada_filtro.clear()

