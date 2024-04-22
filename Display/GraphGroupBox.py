from PySide6.QtWidgets import QGroupBox, QVBoxLayout
from Display.GraphFigure import GraphFigure

class GraphGroupBox(QGroupBox):
    def __init__(self, text):
        super().__init__()
        self.setTitle(text)
        self.main_layout = QVBoxLayout()
        self.figure = GraphFigure(100)
        self.main_layout.addWidget(self.figure)
        self.setLayout(self.main_layout)