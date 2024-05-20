from WaTorSimulation.AnimalsCollector import AnimalsCollector
from Animals.Prey import Prey
from Animals.Predator import Predator
from copy import deepcopy
import numpy as np

class SimulationArea():
    def __init__(self, area_size: int, prey_population, predator_population, a, b, c, d):
        self.area = ([[None for x in range (area_size)] for y in range (area_size)])
        self.animals_collector = AnimalsCollector()
        self.__init_simulation(area_size, prey_population, predator_population, a, b, c, d)

    def __init_simulation(self,area_size, prey_population, predator_population, a, b, c, d):
        self.animals_collector.prepare_sets(self.area, area_size, prey_population, predator_population, a, b, c, d)

    def step(self):
        self.__move_and_update_prey()
        self.__move_and_update_predators()

    def __move_and_update_prey(self):
        prey_new_birth = set()

        for prey in self.animals_collector.prey_set:
            prey.movement(self.area, prey_new_birth)

        if len(prey_new_birth) != 0:
            self.animals_collector.prey_set.update(prey_new_birth)
    
    def __move_and_update_predators(self):
        predator_new_birth = set()
        predator_death = set()
        prey_death = set()

        for predator in self.animals_collector.predator_set:
            predator.movement(self.area, predator_new_birth, predator_death, prey_death)
        
        if len(predator_new_birth) != 0:
            self.animals_collector.predator_set.update(predator_new_birth)
        
        if len(predator_death) != 0:
            self.animals_collector.predator_set.difference_update(predator_death)
        
        if len(prey_death) != 0:
            self.animals_collector.prey_set.difference_update(prey_death)
    
    def end_of_simulation(self):
        result = ( self.__find_value_in_area(1) and self.__find_value_in_area(2))
        return not result

    def __find_value_in_area(self, value):
        area = np.array(self.num_area)
        if np.any(area == value):
            return True
    
    @property
    def prey_count(self):
        return len(self.animals_collector.prey_set)
    
    @property
    def predators_count(self):
        return len(self.animals_collector.predator_set)
    
    @property
    def num_area(self):
        num_matrix = []
        for line in self.area:
            new_line = []
            for value in line:
                if isinstance(value, Prey):
                    new_line.append(1)
                elif isinstance(value, Predator):
                    new_line.append(2)
                else:
                    new_line.append(0)
            num_matrix.append(deepcopy(new_line))
        return num_matrix
            