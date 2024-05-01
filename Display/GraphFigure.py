import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class GraphFigure(FigureCanvasQTAgg):
    def __init__(self, AreaSize=100):
        fig = Figure(figsize=(AreaSize, AreaSize), dpi=100)
        self.__axes = fig.add_subplot(111)
        super(GraphFigure, self).__init__(fig)

    def plot(self, x, y):
        self.__axes.plot(x, y)