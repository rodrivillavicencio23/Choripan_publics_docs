# =============================================================================
# Imports y Modularización
import os
from PyQt6.QtWidgets import (QWidget, QLabel, QVBoxLayout,
                            QHBoxLayout, QPushButton,
                            QScrollArea, QGroupBox, 
                            QLineEdit, QGridLayout)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, pyqtSignal
# =============================================================================

# =============================================================================
# Ventana Principal 
# =============================================================================
class VentanaIndice(QWidget):
    senal_volver_inicio = pyqtSignal()
    senal_ir_mapeado = pyqtSignal()

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.init_gui()
        self.setWindowTitle("DCCORNUCOPIA: INDICE JUGUETES")

    def init_gui(self) -> None:
        self.setFixedSize(720, 720)
        # self.setGeometry(720, 200, 720, 720)

        # ---- IMAGEN DE FONDO ----
        self.fondo = QLabel(self)
        fondo_path = os.path.join("frontend", "images", "gato1.png")
        pixmap = QPixmap(fondo_path)
        self.fondo.setPixmap(pixmap)
        self.fondo.setScaledContents(True)
        self.fondo.setGeometry(0, 0, 720, 720)

        # ---- Ícono de la ventana ----
        self.setWindowIcon(QIcon("frontend/images/gato1.png"))

        # ---- LAYOUT PRINCIPAL VERTICAL ----
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # ---------- IMAGEN DE TÍTULO ----------
        self.titulo_label = QLabel(self)
        self.titulo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)        
        self.titulo_label.setText("DCCORNUCOPIA: INDICE JUGUETES")
        self.titulo_label.setStyleSheet("color: white; font-size: 18px;")

        main_layout.addWidget(self.titulo_label)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # ---------- BLOQUE DE BOTONES ---------- 
        botones = [
            ("Volver Inicio", self.volver_inicio),
            # ("Mapa Estelar", self.ir_mapeado),
            # ("Abrir archivo CSV", self.abrir_archivo),
            # (f"Realizar consulta", self.hacer_consulta)
            ]
        botones_layout = QHBoxLayout()
        botones_layout.addStretch(1)
        for texto, accion in botones:
            btn = QPushButton(texto)
            btn.setFixedSize(325,40)
            btn.setStyleSheet(
                "border: 2px solid rgb(255,255,255);"
                "background-color: rgba(20,20,20,0.9); color: white; "
                "font-family: Times New Roman; font-size: 20px; padding: 10px; ")
            btn.clicked.connect(accion)
            btn.setFixedSize(220, 50)
            botones_layout.addWidget(btn)
        
        # ---- ENTRADA DE TEXTO PARA FILTRO ----
        self.entrada_filtro = QLineEdit(self)
        self.entrada_filtro.setStyleSheet(
            "border: 2px solid rgb(255,255,255);"
            "background-color: rgba(20,20,20, 0.9);"
            "color: yellow; font-size: 12px")
        
        self.texto_entrada_filtro = self.entrada_filtro.text()
        
        botones_layout.addStretch(1)
        main_layout.addLayout(botones_layout) 
        main_layout.addWidget(self.entrada_filtro)

        # ---------- SCROLL DE LISTA ----------
        scroll_group = QGroupBox("Resultados Consulta: ")
        scroll_group.setStyleSheet("color: black; "
                                   "background-color: rgba(255,255,255,0.3)")
        
        scroll_layout = QVBoxLayout(scroll_group)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        contenedor = QWidget()
        grid_scroll = QGridLayout(contenedor) 
        columnas = 3
        for i in range(50):
            label = QLabel(f"ERROR: #{i+1}")
            label.setStyleSheet("color: black; font-weight: bold; "
                                "border: 1px solid gray; padding: 5px;")
            
            fila = i // columnas
            columna = i % columnas

            grid_scroll.addWidget(label, fila, columna)
        
        scroll_area.setWidget(contenedor)
        scroll_layout.addWidget(scroll_area)
        main_layout.addWidget(scroll_group)

        # ---- MAIN LAYOUT ----
        self.setLayout(main_layout)

    # ---------- ACCIONES ----------
    def volver_inicio(self):
        self.hide()
        self.senal_volver_inicio.emit()

# =============================================================================
# =============================================================================
# =============================================================================