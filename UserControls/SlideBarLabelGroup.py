from PySide6.QtWidgets import QWidget, QLabel, QSlider, QSlider, QGroupBox, QHBoxLayout
from PySide6.QtCore import Qt

class SliderLabelGroup(QWidget):
    def __init__(self, text, min_val, max_val):
        super().__init__()

        self.setFixedSize(275, 90)

        self.group_box = QGroupBox(f"{text}")
        self.groupbox_layout = QHBoxLayout(self.group_box)

        self.slider = QSlider(orientation=Qt.Horizontal)
        self.slider.setSingleStep(1)
        self.slider.setMinimum(min_val)
        self.slider.setMaximum(max_val)
        self.slider.setValue(5)
        self.slider.setFixedSize(200, 30)
        self.groupbox_layout.addWidget(self.slider)

        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.group_box)

        self.setLayout(self.main_layout)



