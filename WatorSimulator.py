from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget
from UserControls.ControlPanel import ControlPanel
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QTimer
from Display.SimulatedAreaGroupBox import SimulatedAreaGroupBox
from Display.PopulationsGraphGroupBox import PopulationsGraphGroupBox
from Display.PopulationOverTimeGraphGroupBox import PopulationOverTimeGraphGroupBox
from WaTorSimulation.SimualtionArea import SimulationArea

class UiMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__setup_ui()
    
    def __setup_ui(self):
        self.setWindowTitle("Wator simulatior")
        self.setWindowIcon(QIcon("Graphics/Icon.png"))
        self.setFixedSize(1250, 650)

        self.__simulation_started = False
        self.__main_layout = QHBoxLayout()
        self.__main_window_central_widget = QWidget(self)
        self.__main_window_central_widget.setLayout(self.__main_layout)
        self.setCentralWidget(self.__main_window_central_widget)
        self.__main_layout.setAlignment(Qt.AlignLeft)

        self.__timer = QTimer()
        self.__timer.setInterval(100)
        self.__timer.timeout.connect(self.__simulation_step)

        self.__add_central_panel()
        self.__add_simulated_area_widget()
        self.__add_simulation_graphs()

    def __add_central_panel(self):
        self.__control_panel = ControlPanel()
        self.__control_panel.start_button_clicked_singal.connect(self.__simulation_button_clicked)
        self.__control_panel.reset_button_clicked_singal.connect(self.__reset_simluation)
        self.__control_panel.slider_changed_singal.connect(self.__speed_cange)
        self.__main_layout.addWidget(self.__control_panel)
    
    def __add_simulated_area_widget(self):
        self.__area_groupbox = SimulatedAreaGroupBox()
        self.__area_groupbox.setFixedSize(600,600)
        self.__main_layout.addWidget(self.__area_groupbox)
    
    def __add_simulation_graphs(self):
        self.__population_graph = PopulationsGraphGroupBox("Phase-space plot")
        self.__population_graph.setFixedSize(300,300)

        self.__populationovertime_graph = PopulationOverTimeGraphGroupBox("Populations over time")
        self.__populationovertime_graph.setFixedSize(300,300)

        self.__graphs_layout = QVBoxLayout()
        self.__graphs_layout.addWidget(self.__population_graph)
        self.__graphs_layout.addWidget(self.__populationovertime_graph)
        self.__main_layout.addLayout(self.__graphs_layout)

    def __simulation_button_clicked(self):
        if self.__simulation_started:
            self.__stop_simulation()
        else:
            self.__start_simulation()

    def __start_simulation(self):
        self.__simulation_started = True
        simulation_params = self.__control_panel.simulation_params
        self.__simulation_area = SimulationArea(simulation_params[0], simulation_params[1], simulation_params[2], simulation_params[3],
                                         simulation_params[4],simulation_params[5],simulation_params[6])
        self.__area_groupbox.start_simulation(self.__simulation_area.area)
        self.__population_graph.start_simulation((simulation_params[0]**2) / 4, simulation_params[0]**2)
        self.__populationovertime_graph.start_simulation()
        self.__control_panel.turn_off_widgets()
        self.__timer.setInterval(500 - ((self.__control_panel.speed - 1) * 50))
        self.__timer.start()
            
    def __simulation_step(self):
        self.__simulation_area.step()
        self.__area_groupbox.simulation_step(self.__simulation_area.area)
        self.__population_graph.simulation_step(self.__simulation_area.predators_count, self.__simulation_area.prey_count)
        self.__populationovertime_graph.simulation_step(self.__simulation_area.prey_count, self.__simulation_area.predators_count)
        self.__update_display_widgets()

    def __update_display_widgets(self):
        self.__area_groupbox.update()
        self.__population_graph.update()
        self.__populationovertime_graph.update()

    def __stop_simulation(self):
        self.__simulation_started = False
        self.__timer.stop()
        self.__area_groupbox.stop_simulation()
        self.__population_graph.stop_simulation()
        self.__populationovertime_graph.stop_simulation()
        self.__control_panel.turn_on_widgets()
    
    def __reset_simluation(self):
        if self.__simulation_started == True:
            self.__stop_simulation()


    def __speed_cange(self):
        self.__timer.setInterval(500 - ((self.__control_panel.speed - 1) * 50))
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = UiMainWindow()
    main_window.show()
    sys.exit(app.exec())