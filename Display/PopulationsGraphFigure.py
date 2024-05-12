import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import numpy as np

class PopulationsGraphFigure(FigureCanvasQTAgg):
    def __init__(self, AreaSize, xmax, ymax):
        fig = Figure(figsize=(AreaSize, AreaSize), dpi=100)
        self.__axes = fig.add_subplot(111)
        super(PopulationsGraphFigure, self).__init__(fig)
        self.__xs = []
        self.__ys = []
        self.__xmax = xmax
        self.__ymax = ymax
        self.__alphas = np.linspace(0.1, 1, 35)

    def plot(self, x, y, marks_color):
        self.__axes.cla()
        if len(self.__xs) < 35:
            self.__xs.append(x)
            self.__ys.append(y)
        else:
            xs = self.__xs[1:]
            ys = self.__ys[1:]
            xs.append(x)
            ys.append(y)
            self.__xs = xs
            self.__ys = ys

        self.__axes.set_xticks([])
        self.__axes.set_xlim(0,self.__xmax)
        self.__axes.set_ylim(0,self.__ymax)
        self.__axes.scatter(self.__xs, self.__ys, color = marks_color, alpha=self.__alphas)