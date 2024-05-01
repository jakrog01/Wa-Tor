import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib import colors
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class SimulatedAreaFigure(FigureCanvasQTAgg):
    def __init__(self, area_size):
        fig = Figure(figsize=(area_size, area_size), dpi=100, frameon=False)
        self.__cmap = colors.ListedColormap(['White','Blue','red'])
        self.__axes = fig.add_subplot(111)
        fig.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
        super(SimulatedAreaFigure, self).__init__(fig)
        
    def show_area(self, area):
        self.__axes.clear()
        self.__axes.imshow(area, cmap = self.__cmap)
        self.__axes.axis("off")

