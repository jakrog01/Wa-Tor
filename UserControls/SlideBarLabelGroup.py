from PySide6.QtWidgets import QWidget, QLabel, QSlider, QSlider, QGroupBox, QHBoxLayout
from PySide6.QtCore import Qt

class SliderLabelGroup(QWidget):
    def __init__(self, text, min_val, max_val):
        super().__init__()

        self.setFixedSize(280, 90)

        self.__groupbox = QGroupBox(f"{text}")
        self.__groupbox_layout = QHBoxLayout(self.__groupbox)

        self.__slider = QSlider(orientation=Qt.Horizontal)
        self.__slider.setSingleStep(1)
        self.__slider.setMinimum(min_val)
        self.__slider.setMaximum(max_val)
        self.__slider.setValue(max_val//2)
        self.__slider.setFixedSize(200, 30)
        self.__groupbox_layout.addWidget(self.__slider)

        self.__main_layout = QHBoxLayout()
        self.__main_layout.addWidget(self.__groupbox)

        self.setLayout(self.__main_layout)



