from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget
from UserControls.ControlPanel import ControlPanel
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

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
        
        self.setCentralWidget(self.main_window_central_widget)
        self.main_layout.addWidget(ControlPanel(), alignment=Qt.AlignLeft)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = Ui_main_window()
    main_window.show()
    sys.exit(app.exec())