import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib import colors
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class SimulatedAreaFigure(FigureCanvasQTAgg):
    def __init__(self, area_size, area):
        fig = Figure(figsize=(area_size, area_size), dpi=100, frameon=False)
        cmap = colors.ListedColormap(['White','Blue','red'])
        self.axes = fig.add_subplot(111)
        fig.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
        self.axes.imshow(area, cmap = cmap)
        self.axes.axis("off")
        super(SimulatedAreaFigure, self).__init__(fig)
        

