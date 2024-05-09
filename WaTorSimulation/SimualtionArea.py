from WaTorSimulation.AnimalsCollector import AnimalsCollector
import numpy as np
from time import sleep
from copy import deepcopy

class SimulationArea():
    def __init__(self, area_size: int, prey_population, predator_population, a, b, c, d):
        self.area = np.zeros((area_size, area_size))
        self.animals_collector = AnimalsCollector()
        self.__init_simulation(area_size, prey_population, predator_population, a, b, c, d)

    def __init_simulation(self,area_size, prey_population, predator_population, a, b, c, d):
        self.animals_collector.prepare_sets(self.area, area_size, prey_population, predator_population, a, b, c, d)
        print(len(self.animals_collector.prey_set))
        print(self.area)

    def step(self):
        new_birth = set()
        for prey in self.animals_collector.prey_set:
            prey.move(self.area, new_birth)

        if(len(new_birth)) != 0:
            self.animals_collector.prey_set.update(new_birth)

        print(len(self.animals_collector.prey_set))
        print(self.area)