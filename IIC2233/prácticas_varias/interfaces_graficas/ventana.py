import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
from PyQt6.QtCore import Qt

class GridWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 3x3 Labels")
        self.resize(300, 300)

        # 1. Crear el Layout de cuadrícula
        grid = QGridLayout()
        self.setLayout(grid)

        # 2. Crear y añadir labels (filas y columnas van de 0 a 2 para 3x3)
        positions = [(i, j) for i in range(4) for j in range(3)]
        
        for position in positions:
            label = QLabel(f"Label {position[0]+1},{position[1]+1}")
            # Estilo básico para visualizarlos mejor
            label.setStyleSheet("border: 1px solid black; background-color: white;")
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            # grid.addWidget(widget, fila, columna)
            grid.addWidget(label, *position)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GridWindow()
    window.show()
    sys.exit(app.exec())
