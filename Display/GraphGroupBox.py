from PySide6.QtWidgets import QGroupBox, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from Display.GraphFigure import GraphFigure

class GraphGroupBox(QGroupBox):
    def __init__(self, text):
        super().__init__()
        self.setTitle(text)
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignCenter)
        self.Picture_Label = QLabel()
        pixmap = QPixmap("Graphics/Icon.png")
        pixmap = pixmap.scaled(250, 250, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.Picture_Label.setPixmap(pixmap)
        self.main_layout.addWidget(self.Picture_Label)
        self.setLayout(self.main_layout)

    def start_simulation(self):
        for i in reversed(range(self.main_layout.count())): 
            self.main_layout.itemAt(i).widget().setParent(None)

        self.figure = GraphFigure(100)
        self.main_layout.addWidget(self.figure)