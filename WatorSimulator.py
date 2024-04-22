from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget
from UserControls.ControlPanel import ControlPanel
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from Display.SimulatedAreaGroupBox import SimulatedAreaGroupBox
from Display.GraphGroupBox import GraphGroupBox

class Ui_main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
    def setupUi(self, main_window):
        main_window.setWindowTitle("Wator simulatior")
        main_window.setWindowIcon(QIcon("Graphics/Icon.png"))
        main_window.setFixedSize(1220, 650)

        self.main_layout = QHBoxLayout()
        self.main_window_central_widget = QWidget(main_window)
        self.main_window_central_widget.setLayout(self.main_layout)

        self.groupbox = SimulatedAreaGroupBox()
        self.groupbox.setFixedSize(600,600)

        self.population_graph = GraphGroupBox("Phase-space plot")
        self.population_graph.setFixedSize(250,250)

        self.populationovertime_graph = GraphGroupBox("Populations over time")
        self.populationovertime_graph.setFixedSize(250,250)

        self.graphs_layout = QVBoxLayout()
        self.graphs_layout.addWidget(self.population_graph)
        self.graphs_layout.addWidget(self.populationovertime_graph)

        self.setCentralWidget(self.main_window_central_widget)
        self.main_layout.setAlignment(Qt.AlignLeft)
        self.main_layout.addWidget(ControlPanel())
        self.main_layout.addWidget(self.groupbox)
        self.main_layout.addLayout(self.graphs_layout)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = Ui_main_window()
    main_window.show()
    sys.exit(app.exec())