from WaTorSimulation.AnimalsCollector import AnimalsCollector
import numpy as np

class SimulationArea():
    def __init__(self, area_size, collector):
        self.area = np.zeros((area_size, area_size))
        self.animals_collector= collector