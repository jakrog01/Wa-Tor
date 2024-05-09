from PySide6.QtWidgets import QGroupBox, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from Display.SimulatedAreaFigure import SimulatedAreaFigure

class SimulatedAreaGroupBox(QGroupBox):
    def __init__(self):
        super().__init__()
        self.setTitle("Simulation area")
        self.__main_layout = QVBoxLayout()
        self.__main_layout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.__main_layout)
        self.__draw_logo_image()
    
    def __clear_main_layout(self):
        for i in reversed(range(self.__main_layout.count())): 
            self.__main_layout.itemAt(i).widget().setParent(None)

    def __draw_logo_image(self):
        self.__clear_main_layout()
        self.__Picture_Label = QLabel()
        pixmap = QPixmap("Graphics/Icon.png")
        pixmap = pixmap.scaled(550, 550, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.__Picture_Label.setPixmap(pixmap)
        self.__main_layout.addWidget(self.__Picture_Label)

    def start_simulation(self, area):
        self.__clear_main_layout()
        self.__figure = SimulatedAreaFigure(100)
        self.__main_layout.addWidget(self.__figure)
        self.simulation_step(area)
    
    def simulation_step(self, area):
        self.__figure.show_area(area)
        self.__figure.draw()
    
    def stop_simulation(self):
        self.__draw_logo_image()
        