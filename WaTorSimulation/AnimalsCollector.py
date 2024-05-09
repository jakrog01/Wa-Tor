from Animals.Prey import Prey
from Animals.Predator import Predator
from random import randint
import math

class AnimalsCollector():
    def __init__(self):
        self.predator_set = set()
        self.prey_set = set()
    
    def prepare_sets(self, area, area_size, prey_population_percent, predator_population_percent, a, b, c, d):
        init_cords_set = set()
        prey_population = math.floor((prey_population_percent/100) * area_size**2)
        predator_population = math.floor((predator_population_percent/100) * area_size**2) 

        while len(init_cords_set) < prey_population + predator_population:
            init_cords_set.add((randint(0,area_size-1), randint(0,area_size-1)))
        
        for index, cords in enumerate(init_cords_set):
            if index < prey_population:
                self.prey_set.add(Prey(area_size, cords[0], cords[1], a))
                area[cords[1]][cords[0]] = 1
            else:
                self.predator_set.add(Predator(cords[0], cords[1], b, c, d))
                area[cords[1]][cords[0]] = 2

