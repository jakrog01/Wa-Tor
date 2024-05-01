from WaTorSimulation.AnimalsCollector import AnimalsCollector
import numpy as np

class SimulationArea():
    def __init__(self, area_size: int, prey_population, predator_population, a, b, c, d):
        self.area = np.zeros((area_size, area_size))
        self.animals_collector = AnimalsCollector()
        self.__init_simulation(area_size, prey_population, predator_population, a, b, c, d)

    def __init_simulation(self,area_size, prey_population, predator_population, a, b, c, d):
        self.animals_collector.prepare_sets(self.area, area_size, prey_population, predator_population, a, b, c, d)
