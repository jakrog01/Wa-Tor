from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QPushButton
from UserControls.SpinBoxLabelGroup import SpinBoxLabelGroup
from UserControls.SlideBarLabelGroup import SliderLabelGroup
from PySide6.QtCore import Qt, Signal


class ControlPanel(QWidget):
    start_button_clicked_singal = Signal()
    slider_changed_singal = Signal()

    def __init__(self):
        super().__init__()
        self.setFixedWidth(320)
        self.__main_layout = QVBoxLayout()
        self.setLayout(self.__main_layout)
        self.__add_button_layout()
        self.__add_simulation_controls()

    def __add_button_layout(self):
        self.__button_layout = QHBoxLayout()

        self.__start_button = QPushButton()
        self.__start_button.setText("START")
        self.__start_button.setFixedSize(130,40)
        self.__start_button.clicked.connect(self.__start_button_clicked)
        self.__simulation_action = {"START": self.__start_simulation, "STOP": self.__stop_simulation}
        self.__button_layout.addWidget(self.__start_button)

        self.__reset_button = QPushButton("RESET")
        self.__reset_button.setFixedSize(130,40)
        self.__button_layout.addWidget(self.__reset_button)

        self.__main_layout.addLayout(self.__button_layout)

    def __add_simulation_controls(self):
        self.__simulation_control_layout = QVBoxLayout()
        self.__simulation_control_layout.setAlignment(Qt.AlignLeft)
        self.__simulation_control_layout.setContentsMargins(0,0,0,0)
        self.__scroll_area = QScrollArea()
        self.__scroll_area.setWidgetResizable(True)
        self.__scroll_area.setFixedWidth(300)
        self.__scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.__main_layout.addWidget(self.__scroll_area)
        
        scroll_content = QWidget()
        scroll_content.setLayout(self.__simulation_control_layout)
        self.__speed_slider = SliderLabelGroup("Simulation speed:", 0, 10)
        self.__speed_slider.slider_edit_finished_singal.connect(self.__emit_edit_slider)
        self.__simulation_control_layout.addWidget(self.__speed_slider)
        params_label = QLabel("SIMULATION PARAMTERS")

        self.__simulation_control_layout.addWidget(params_label, alignment=Qt.AlignCenter)
        self.__scroll_area.setWidget(scroll_content)
        self.__add_parameters_controls()

    def __add_parameters_controls(self):
        self.__parameters_layout = QVBoxLayout()

        self.__area_size_spinbox = SpinBoxLabelGroup("Area size", "Size of simualtion area:", 10, 150)
        self.__parameters_layout.addWidget(self.__area_size_spinbox)

        self.__prey_population_spinbox = SpinBoxLabelGroup("Prey population", "Initial prey density (%):", 0, 100)
        self.__prey_population_spinbox.spinbox_edit_finished_singal.connect(self.__spinbox_change)
        self.__parameters_layout.addWidget(self.__prey_population_spinbox)

        self.__predator_population_spinbox = SpinBoxLabelGroup("Predator population", "Initial predator density (%):", 0, 100)
        self.__predator_population_spinbox.spinbox_edit_finished_singal.connect(self.__spinbox_change)
        self.__parameters_layout.addWidget(self.__predator_population_spinbox)
        
        self.__param_a_spinbox = SpinBoxLabelGroup("a", "Prey propagation (steps):", 0, 10)
        self.__parameters_layout.addWidget(self.__param_a_spinbox)

        self.__param_b_spinbox = SpinBoxLabelGroup("b", "Hunting effectiveness (%):", 0, 100)
        self.__parameters_layout.addWidget(self.__param_b_spinbox)
        
        self.__param_c_spinbox = SpinBoxLabelGroup("c", "Predator death rate (steps):", 0, 10)
        self.__parameters_layout.addWidget(self.__param_c_spinbox)

        self.__param_d_spinbox = SpinBoxLabelGroup("d", "Predator propagation (steps):", 0, 20)
        self.__parameters_layout.addWidget(self.__param_d_spinbox)

        self.__simulation_control_layout.addLayout(self.__parameters_layout)

    def __start_button_clicked(self):
        self.__simulation_action[self.__start_button.text()]()
    
    def __spinbox_change(self, value):
        sum = self.__predator_population_spinbox.value + self.__prey_population_spinbox.value 
        if sum > 100:
            if value == "Prey population":
                self.__predator_population_spinbox.value =  self.__predator_population_spinbox.value - (sum - 100)
            else:
                self.__prey_population_spinbox.value =  self.__prey_population_spinbox.value - (sum - 100)
    
    def __start_simulation(self):
        self.__start_button.setText("STOP")
        self.start_button_clicked_singal.emit()
    
    def __stop_simulation(self):
        self.__start_button.setText("START")
        self.start_button_clicked_singal.emit()

    def turn_off_widgets(self):
        for i in reversed(range(self.__parameters_layout.count())): 
            self.__parameters_layout.itemAt(i).widget().turn_off_widgets()
    
    def turn_on_widgets(self):
        for i in reversed(range(self.__parameters_layout.count())): 
            self.__parameters_layout.itemAt(i).widget().turn_on_widgets()
    
    def __emit_edit_slider(self):
        self.slider_changed_singal.emit()

    @property
    def simulation_params(self):
        return (self.__area_size_spinbox.value, self.__prey_population_spinbox.value, self.__predator_population_spinbox.value,
                self.__param_a_spinbox.value, self.__param_b_spinbox.value, self.__param_c_spinbox.value, 
                self.__param_d_spinbox.value)
    
    @property
    def speed(self):
        return self.__speed_slider.value
        
        
        


