from PySide6.QtWidgets import QWidget, QLabel, QSpinBox, QSlider, QGroupBox, QHBoxLayout
from PySide6.QtCore import Qt, Signal

class SpinBoxLabelGroup(QWidget):
    spinbox_edit_finished_singal = Signal(str)

    def __init__(self, text, label_text, min_val, max_val, def_value):
        super().__init__()
        self.__default_value = def_value
        self.setFixedSize(280, 90)

        self.__groupbox = QGroupBox(f"{text}")
        self.__groupbox_layout = QHBoxLayout(self.__groupbox)

        label = QLabel(label_text)
        self.__spinbox = QSpinBox()
        self.__spinbox.setMinimum(min_val)
        self.__spinbox.setMaximum(max_val)
        self.__spinbox.setSingleStep(1)
        self.__spinbox.setValue(self.__default_value)
        self.__spinbox.setFixedSize(80, 30)
        self.__spinbox.valueChanged.connect(self.__emit_edit_finished_singal)

        self.__groupbox_layout.addWidget(label)
        self.__groupbox_layout.addWidget(self.__spinbox)

        self.__main_layout = QHBoxLayout()
        self.__main_layout.addWidget(self.__groupbox)

        self.setLayout(self.__main_layout)

    def turn_off_widgets(self):
        self.__spinbox.setEnabled(False)
    
    def turn_on_widgets(self):
        self.__spinbox.setEnabled(True)
    
    def __emit_edit_finished_singal(self):
        self.spinbox_edit_finished_singal.emit(self.__groupbox.title())

    @property
    def value(self):
        return int(self.__spinbox.value())
    
    @value.setter
    def value(self, new_value):
        self.__spinbox.setValue(new_value)


