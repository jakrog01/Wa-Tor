from abc import ABC, abstractmethod

class AbstractRespectToStrategy():
    def __init__(self):
        pass
    
    @abstractmethod
    def start_analysis(self, area_sizes_tuple, init_prey_populations_tuple, init_predators_populations_tuple, 
                        a_params_tuple, b_params_tuple, c_params_tuple, d_params_tuple):
        pass