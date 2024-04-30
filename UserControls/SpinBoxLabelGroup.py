from PySide6.QtWidgets import QWidget, QLabel, QSpinBox, QSlider, QGroupBox, QHBoxLayout
from PySide6.QtCore import Qt

class SpinBoxLabelGroup(QWidget):
    def __init__(self, text, label_text, min_val, max_val):
        super().__init__()

        self.setFixedSize(280, 90)

        self.__groupbox = QGroupBox(f"{text}")
        self.__groupbox_layout = QHBoxLayout(self.__groupbox)

        label = QLabel(label_text)
        self.__spinbox = QSpinBox()
        self.__spinbox.setMinimum(min_val)
        self.__spinbox.setMaximum(max_val)
        self.__spinbox.setSingleStep(1)
        self.__spinbox.setValue(max_val//2)
        self.__spinbox.setFixedSize(80, 30)

        self.__groupbox_layout.addWidget(label)
        self.__groupbox_layout.addWidget(self.__spinbox)

        self.__main_layout = QHBoxLayout()
        self.__main_layout.addWidget(self.__groupbox)

        self.setLayout(self.__main_layout)

    def turn_off_widgets(self):
        self.__spinbox.setEnabled(False)



