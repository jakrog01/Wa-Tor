from WaTorSimulation.AnimalsCollector import AnimalsCollector
from copy import deepcopy
import numpy as np

class SimulationArea():
    def __init__(self, area_size: int, collector: AnimalsCollector):
        self.area = np.zeros((area_size, area_size))
        self.animals_collector = collector

    def move_animals(self):
        for prey in self.animals_collector.prey_set:
            pass
        
        for predator in self.animals_collector.predator_set:
            pass
