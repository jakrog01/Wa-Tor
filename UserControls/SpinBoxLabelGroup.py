from PySide6.QtWidgets import QWidget, QLabel, QSpinBox, QSlider, QGroupBox, QHBoxLayout
from PySide6.QtCore import Qt

class SpinBoxLabelGroup(QWidget):
    def __init__(self, text, label_text, min_val, max_val):
        super().__init__()

        self.setFixedSize(275, 90)

        self.group_box = QGroupBox(f"{text}")
        self.groupbox_layout = QHBoxLayout(self.group_box)

        label = QLabel(label_text)
        self.spinbox = QSpinBox()
        self.spinbox.setMinimum(min_val)
        self.spinbox.setMaximum(max_val)
        self.spinbox.setFixedSize(80, 30)

        self.groupbox_layout.addWidget(label)
        self.groupbox_layout.addWidget(self.spinbox)

        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.group_box)

        self.setLayout(self.main_layout)



