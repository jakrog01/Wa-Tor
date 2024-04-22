from PySide6.QtWidgets import QGroupBox, QVBoxLayout
from Display.SimulatedAreaFigure import SimulatedAreaFigure

class SimulatedAreaGroupBox(QGroupBox):
    def __init__(self):
        super().__init__()
        self.setTitle("Simulation area")
        self.main_layout = QVBoxLayout()
        self.figure = SimulatedAreaFigure(100)
        self.main_layout.addWidget(self.figure)
        self.setLayout(self.main_layout)