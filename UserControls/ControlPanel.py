from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QPushButton
from UserControls.SpinBoxLabelGroup import SpinBoxLabelGroup
from UserControls.SlideBarLabelGroup import SliderLabelGroup
from PySide6.QtCore import Qt

#MainArea 550x550
#Charts 175x175

class ControlPanel(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(320)

        self.button_layout = QHBoxLayout()
        self.start_button = QPushButton("START")
        self.start_button.setFixedSize(130,40)
        self.button_layout.addWidget(self.start_button)

        self.reset_button = QPushButton("RESET")
        self.reset_button.setFixedSize(130,40)
        self.button_layout.addWidget(self.reset_button)

        self.parameters_layout = QVBoxLayout()
        self.parameters_layout.setAlignment(Qt.AlignLeft)
        self.setLayout(self.parameters_layout)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFixedWidth(300)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.parameters_layout.setContentsMargins(0,0,0,0)

        scroll_content = QWidget()

        scroll_content.setLayout(self.parameters_layout)
        self.scroll_area.setWidget(scroll_content)

        self.params_label = QLabel("SIMULATION PARAMETERS")

        self.parameters_layout.addWidget(SliderLabelGroup("Simulation speed:", 50, 150))
        self.parameters_layout.addWidget(self.params_label, alignment=Qt.AlignCenter)
        self.parameters_layout.addWidget(SpinBoxLabelGroup("Area size", "Size of simualtion area:", 50, 150))
        self.parameters_layout.addWidget(SpinBoxLabelGroup("Prey population", "Initial prey density (%):", 50, 150))
        self.parameters_layout.addWidget(SpinBoxLabelGroup("Predator population", "Initial predator density (%):", 50, 150))
        self.parameters_layout.addWidget(SpinBoxLabelGroup("a", "Prey propagation:", 50, 150))
        self.parameters_layout.addWidget(SpinBoxLabelGroup("b", "Hunting effectiveness:", 50, 150))
        self.parameters_layout.addWidget(SpinBoxLabelGroup("c", "Predator death rate:", 50, 150))
        self.parameters_layout.addWidget(SpinBoxLabelGroup("d", "Predator propagation:", 50, 150))
        
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addWidget(self.scroll_area)
        self.setLayout(self.main_layout)
        
        
        


