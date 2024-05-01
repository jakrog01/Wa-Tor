from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget
from UserControls.ControlPanel import ControlPanel
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from Display.SimulatedAreaGroupBox import SimulatedAreaGroupBox
from Display.GraphGroupBox import GraphGroupBox
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

        self.__add_central_panel()
        self.__add_simulated_area_widget()
        self.__add_simulation_graphs()

    def __add_central_panel(self):
        self.__control_panel = ControlPanel()
        self.__control_panel.start_button_clicked_singal.connect(self.__simulation_button_clicked)
        self.__main_layout.addWidget(self.__control_panel)
    
    def __add_simulated_area_widget(self):
        self.__area_groupbox = SimulatedAreaGroupBox()
        self.__area_groupbox.setFixedSize(600,600)
        self.__main_layout.addWidget(self.__area_groupbox)
    
    def __add_simulation_graphs(self):
        self.__population_graph = GraphGroupBox("Phase-space plot")
        self.__population_graph.setFixedSize(300,300)

        self.__populationovertime_graph = GraphGroupBox("Populations over time")
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
        simulation_area = SimulationArea(simulation_params[0], simulation_params[1], simulation_params[2], simulation_params[3],
                                         simulation_params[4],simulation_params[5],simulation_params[6])
        self.__area_groupbox.start_simulation(simulation_area.area)
        self.__population_graph.start_simulation()
        self.__populationovertime_graph.start_simulation()
        self.__control_panel.turn_off_widgets()

    def __stop_simulation(self):
        self.__simulation_started = False
        self.__area_groupbox.stop_simulation()
        self.__population_graph.stop_simulation()
        self.__populationovertime_graph.stop_simulation()
        self.__control_panel.turn_on_widgets()
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = UiMainWindow()
    main_window.show()
    sys.exit(app.exec())