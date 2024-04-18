from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QIcon

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Wator simulatior")
        MainWindow.setWindowIcon(QIcon("Graphics/Icon.png"))
        MainWindow.setFixedSize(1020, 600)

        


if __name__ == "__main__": #main
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())