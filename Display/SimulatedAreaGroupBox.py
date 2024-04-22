from PySide6.QtWidgets import QGroupBox, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from Display.SimulatedAreaFigure import SimulatedAreaFigure

class SimulatedAreaGroupBox(QGroupBox):
    def __init__(self):
        
        self.area = [[0 for x in range(100)] for y in range (100)]
        self.area[0][0] = 1
        self.area[99][99] = 2
        super().__init__()
        self.setTitle("Simulation area")
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignCenter)
        self.Picture_Label = QLabel()
        pixmap = QPixmap("Graphics/Icon.png")
        pixmap = pixmap.scaled(550, 550, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.Picture_Label.setPixmap(pixmap)
        self.main_layout.addWidget(self.Picture_Label)
        self.setLayout(self.main_layout)

    def start_simulation(self):
        for i in reversed(range(self.main_layout.count())): 
            self.main_layout.itemAt(i).widget().setParent(None)

        self.figure = SimulatedAreaFigure(100, self.area)
        self.main_layout.addWidget(self.figure)
        