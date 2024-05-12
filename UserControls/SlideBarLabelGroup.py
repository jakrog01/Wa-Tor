from PySide6.QtWidgets import QWidget, QLabel, QSlider, QSlider, QGroupBox, QHBoxLayout
from PySide6.QtCore import Qt, Signal

class SliderLabelGroup(QWidget):
    slider_edit_finished_singal = Signal()

    def __init__(self, text, min_val, max_val, def_value):
        super().__init__()
        self.__default_value = def_value
        self.setFixedSize(280, 90)

        self.__groupbox = QGroupBox(f"{text}")
        self.__groupbox_layout = QHBoxLayout(self.__groupbox)

        self.__slider = QSlider(orientation=Qt.Horizontal)
        self.__slider.setSingleStep(1)
        self.__slider.setMinimum(min_val)
        self.__slider.setMaximum(max_val)
        self.__slider.setValue(self.__default_value)
        self.__slider.setFixedSize(200, 30)
        self.__groupbox_layout.addWidget(self.__slider)
        self.__slider.valueChanged.connect(self.__emit_edit_finished_singal)
        self.__main_layout = QHBoxLayout()
        self.__main_layout.addWidget(self.__groupbox)

        self.setLayout(self.__main_layout)
    
    def __emit_edit_finished_singal(self):
        self.slider_edit_finished_singal.emit()

    @property
    def value(self):
        return int(self.__slider.value())


