from AnalysisScripts.Strategies.RespectToStrategies.AbstractRespectToStrategy import AbstractRespectToStrategy
import matplotlib.pyplot as plt
from WaTorSimulation.SimualtionArea import SimulationArea
from multiprocessing import Pool
import numpy as np
from copy import deepcopy

class RespectToAreaSizeStrategy(AbstractRespectToStrategy):
    def __init__(self, errorbars: bool, threads_count, count_to_average, iteration_per_step):
        self.__error_bars = errorbars
        self.__threads_count = threads_count
        self.__count_to_average = count_to_average
        self.__iteration_per_step = iteration_per_step

    def start_analysis(self, area_sizes_tuple, init_prey_populations_tuple, init_predators_populations_tuple, 
                        a_params_tuple, b_params_tuple, c_params_tuple, d_params_tuple):
            
            self.__area_sizes = list(area_sizes_tuple)
            self.__area_sizes.sort()
            self.__prepare_parameters_list(init_prey_populations_tuple, init_predators_populations_tuple, a_params_tuple, 
                                        b_params_tuple, c_params_tuple, d_params_tuple)
            
            for parameters in self.__parameters_list:
                self.__run_analysis(parameters)
    
    def __prepare_parameters_list(self, init_prey_populations_tuple, init_predators_populations_tuple, a_params_tuple,
                                  b_params_tuple, c_params_tuple, d_params_tuple):
        
        self.__parameters_list = []
        for init_prey_population in init_prey_populations_tuple:
            for init_predator_population in init_predators_populations_tuple:
                for a_param in a_params_tuple:
                    for b_param in b_params_tuple:
                        for c_param in c_params_tuple:
                            for d_param in d_params_tuple:
                                self.__parameters_list.append([init_prey_population, init_predator_population, a_param,
                                                                b_param, c_param, d_param])
                                
    def __run_analysis(self, params_list):
        pool_results = [[None for _ in range(self.__count_to_average)] for __ in range (len(self.__area_sizes))]
        
        if self.__threads_count > 0:
            pool = Pool(processes= self.__threads_count)
        else:
            pool = Pool()

        for area_size_index, area_size in enumerate(self.__area_sizes):
            if (params_list[0] + params_list[1]) > 100:
                print("PROBLEM WITH SIMULATION PARAMS")
                return
            for average_index in range(self.__count_to_average):
                area = SimulationArea(area_size, params_list[0], params_list[1], params_list[2], params_list[3], params_list[4], 
                                      params_list[5])
                pool_results[area_size_index][average_index] = pool.apply_async(self.perform_single_simulation, args=(deepcopy(area), ))
        pool.close()
        pool.join()

        output_values = [[result.get() for result in results] for results in pool_results]

        result = []
        result_std = []

        for values in output_values:
            result.append(np.mean(values))
            result_std.append(np.std(values))

        if self.__error_bars:
            self.__save_result_with_bars(result, result_std, params_list)
        else:
            self.__save_result_without_bars(result, params_list)
    
    def perform_single_simulation(self, area):
        for i in range(self.__iteration_per_step):
            area.step()
            if area.end_of_simulation():
                return (i+1)
        return (self.__iteration_per_step)
    
    def __save_result_with_bars(self, result, result_std, params_list):
        threshold = 0
        max = 0
        
        for index,b in enumerate(result):
            if b == self.__iteration_per_step:
                threshold = self.__area_sizes[index]
                break
            elif b > max:
                max = b
                threshold = self.__area_sizes[index]

        plt.errorbar(self.__area_sizes, result, yerr= result_std)
        plt.axvline(threshold, linestyle='-.', linewidth = 1, label = f"Threshold value = {round(threshold,2)}%", color = "grey")
        plt.xlabel("Area size")
        plt.ylabel("Number of iterations")
        plt.savefig(f"AnalysisResults/png/AS{params_list[0]}_{params_list[1]}_{params_list[2]}_{params_list[3]}_{params_list[4]}_{params_list[5]}Graph{self.__iteration_per_step}_{self.__count_to_average}")
        plt.cla()

        with open(f"AnalysisResults/txt/AS{params_list[0]}_{params_list[1]}_{params_list[2]}_{params_list[3]}_{params_list[4]}_{params_list[5]}Results{self.__iteration_per_step}_{self.__count_to_average}.txt", 'w') as f:
            f.write(f"numbers_of_iteration= {result}")
            f.write("\n")
            f.write("\n")
            f.write(f"numbers_of_iteration_std= {result_std}")
    
    def __save_result_without_bars(self, result, params_list):
        threshold = 0
        max = 0
        
        for index,area_size in enumerate(result):
            if area_size == self.__iteration_per_step:
                threshold = self.__area_sizes[index]
                break
            elif area_size > max:
                max = area_size
                threshold = self.__area_sizes[index]

        plt.scatter(self.__area_sizes, result)
        plt.axvline(threshold, linestyle='-.', linewidth = 1, label = f"Threshold value = {round(threshold,2)}%", color = "grey")
        plt.xlabel("Area size")
        plt.ylabel("Number of iterations")
        plt.savefig(f"AnalysisResults/png/AS{params_list[0]}_{params_list[1]}_{params_list[2]}_{params_list[3]}_{params_list[4]}_{params_list[5]}Graph{self.__iteration_per_step}_{self.__count_to_average}")
        plt.cla()

        with open(f"AnalysisResults/txt/AS{params_list[0]}_{params_list[1]}_{params_list[2]}_{params_list[3]}_{params_list[4]}_{params_list[5]}Results{self.__iteration_per_step}_{self.__count_to_average}.txt", 'w') as f:
            f.write(f"numbers_of_iteration= {result}")