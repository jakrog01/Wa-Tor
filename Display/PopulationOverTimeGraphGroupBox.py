from PySide6.QtWidgets import QGroupBox, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from Display.PopulationOverTimeGraphFigure import PopulationOverTimeGraphFigure

class PopulationOverTimeGraphGroupBox(QGroupBox):
    def __init__(self, text):
        super().__init__()
        self.setTitle(text)
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
        pixmap = pixmap.scaled(250, 250, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.__Picture_Label.setPixmap(pixmap)
        self.__main_layout.addWidget(self.__Picture_Label)

    def start_simulation(self, area_size):
        self.__clear_main_layout()
        self.__figure = PopulationOverTimeGraphFigure(area_size)
        self.__main_layout.addWidget(self.__figure)
        self.__figure.plot(0, 0)

    def simulation_step(self, yprey, ypredators):
        self.__figure.plot(yprey, ypredators)
        self.__figure.draw()
    
    def stop_simulation(self):
        self.__draw_logo_image()