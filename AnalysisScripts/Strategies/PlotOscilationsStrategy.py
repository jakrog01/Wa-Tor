import matplotlib.pyplot as plt
from WaTorSimulation.SimualtionArea import SimulationArea
from multiprocessing import Pool
import numpy as np
from copy import deepcopy

class PlotOscilationInTimeStrategy():
    def __init__(self, errorbars: bool, threads_count, count_to_average, iteration_per_step):
        self.__error_bars = errorbars
        self.__threads_count = threads_count
        self.__count_to_average = count_to_average
        self.__iteration_per_step = iteration_per_step

    def start_analysis(self, area_sizes_tuple, init_prey_populations_tuple, init_predators_populations_tuple, 
                       a_params_tuple, b_params_tuple, c_params_tuple, d_params_tuple):
        
        self.__prepare_parameters_list(area_sizes_tuple, init_prey_populations_tuple, init_predators_populations_tuple, 
                                       a_params_tuple, b_params_tuple, c_params_tuple, d_params_tuple)
        
        for parameters in self.__parameters_list:
            self.__run_analysis(parameters)

    def __prepare_parameters_list(self, area_sizes_tuple, init_prey_populations_tuple, init_predators_populations_tuple, 
                                  a_params_tuple, b_params_tuple, c_params_tuple, d_params_tuple):
        
        self.__parameters_list = []

        for area_size in area_sizes_tuple:
            for init_prey_population in init_prey_populations_tuple:
                for init_predator_population in init_predators_populations_tuple:
                    for a_param in a_params_tuple:
                        for b_param in b_params_tuple:
                            for c_param in c_params_tuple:
                                for d_param in d_params_tuple:
                                    self.__parameters_list.append([area_size, init_prey_population, init_predator_population,
                                                                   a_param, b_param, c_param, d_param])

    def __run_analysis(self, params_list):

        pool_results = [None for _ in range(self.__count_to_average)]

        if self.__threads_count > 0:
            pool = Pool(processes= self.__threads_count)
        else:
            pool = Pool()

        for average_index in range(self.__count_to_average):
            area = SimulationArea(params_list[0], params_list[1], params_list[2], params_list[3], params_list[4], 
                                    params_list[5], params_list[6])
            pool_results[average_index] = pool.apply_async(self.perform_single_simulation, args=(deepcopy(area), ))

        pool.close()
        pool.join()

        output_values = np.array([result.get() for result in pool_results])

        prey_results = [x for x,y in output_values]
        predators_results = [y for x,y in output_values]

        prey_result = np.mean(prey_results, axis=0)
        prey_result_std = np.std(prey_results, axis=0)

        predators_result = np.mean(predators_results, axis=0)
        predators_result_std = np.std(predators_results, axis=0)

        if self.__error_bars:
            self.__save_result_with_bars(prey_result, prey_result_std, predators_result, predators_result_std, params_list)
        else:
            self.__save_result_without_bars(prey_result, predators_result, params_list)
    
    def perform_single_simulation(self, area:SimulationArea):
        prey_result = []
        predators_result = []
        for i in range(self.__iteration_per_step):
            area.step()
            prey_result.append(area.prey_count)
            predators_result.append(area.predators_count)
        
        return (prey_result, predators_result)
    
    def __save_result_with_bars(self, prey_result, prey_result_std, predators_result, predators_result_std, params_list):
        iterations = [x for x in range (len(prey_result))]
        plt.errorbar(iterations, prey_result, yerr= prey_result_std, color = "blue", label= "Prey")
        plt.errorbar(iterations, predators_result, yerr= predators_result_std, color = "red", label= "Predators")
        plt.legend()
        plt.xlabel("Simulation step")
        plt.ylabel("Population size")
        plt.savefig(f"AnalysisResults/png/O{params_list[0]}_{params_list[1]}_{params_list[2]}_{params_list[3]}_{params_list[4]}_{params_list[5]}_{params_list[6]}Graph{self.__iteration_per_step}_{self.__count_to_average}")
        plt.cla()

        with open(f"AnalysisResults/txt/O{params_list[0]}_{params_list[1]}_{params_list[2]}_{params_list[3]}_{params_list[4]}_{params_list[5]}_{params_list[6]}Results{self.__iteration_per_step}.txt", 'w') as f:
            f.write(f"prey_list = {prey_result}")
            f.write(f"prey_std_list = {prey_result_std}")
            f.write("\n")
            f.write("\n")
            f.write(f"predator_list = {predators_result}")
            f.write(f"predator_std_list = {predators_result_std}")
    
    def __save_result_without_bars(self, prey_result, predators_result, params_list):
        iterations = [x for x in range (len(prey_result))]
        plt.scatter(iterations, prey_result, color = "blue", label= "Prey", s = 5)
        plt.scatter(iterations, predators_result, color = "red", label= "Predators", s = 5)
        plt.legend()
        plt.xlabel("Simulation step")
        plt.ylabel("Population size")
        plt.savefig(f"AnalysisResults/png/O{params_list[0]}_{params_list[1]}_{params_list[2]}_{params_list[3]}_{params_list[4]}_{params_list[5]}_{params_list[6]}Graph{self.__iteration_per_step}_{self.__count_to_average}")
        plt.cla()

        with open(f"AnalysisResults/txt/O{params_list[0]}_{params_list[1]}_{params_list[2]}_{params_list[3]}_{params_list[4]}_{params_list[5]}_{params_list[6]}Results{self.__iteration_per_step}.txt", 'w') as f:
            f.write(f"prey_list = {prey_result}")
            f.write("\n")
            f.write("\n")
            f.write(f"predator_list = {predators_result}")

