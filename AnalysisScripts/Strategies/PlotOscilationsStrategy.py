import matplotlib.pyplot as plt
from WaTorSimulation.SimualtionArea import SimulationArea
from multiprocessing import Pool
import numpy as np

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
        
        pool = Pool()
        for index, params_lsit in enumerate(self.__parameters_list):
            pool.apply_async(self.create_graph, args=(self.__parameters_list[index], ))
        pool.close()
        pool.join()

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

    def create_graph(self, params_list):
        area = SimulationArea(params_list[0], params_list[1], params_list[2], params_list[3],
                              params_list[4], params_list[5], params_list[6])
        prey_counts = []
        prey_counts_std = []
        predator_counts = []
        predator_counts_std = []

        iterations = [(x+1) for x in range(self.__iteration_per_step)]

        for iteration in range(self.__iteration_per_step):
            area.step()
            prey_counts_to_average = []
            predators_counts_to_average = []

            for average in range (self.__count_to_average):
                prey_counts_to_average.append(area.prey_count)
                predators_counts_to_average.append(area.predators_count)

            prey_counts.append(np.mean(prey_counts_to_average))
            predator_counts.append(np.mean(predators_counts_to_average))
            prey_counts_std.append(np.std(prey_counts_to_average))
            predator_counts_std.append(np.std(predators_counts_to_average))

            if self.__error_bars:
                self.__plot_result_with_bars(iterations, prey_counts, prey_counts_std, predator_counts, predator_counts_std, params_list)
            else:
                self.__plot_result_without_bars(iterations, prey_counts, predator_counts, params_list)

    def __plot_result_with_bars(self, iterations, prey_counts, prey_counts_std, predator_counts, predator_counts_std, params_list):
        plt.errorbar(iterations, prey_counts, yerr= prey_counts_std, color = "blue", label = "Prey population")
        plt.errorbar(iterations, predator_counts, yerr= predator_counts_std, color = "red", label = "Predator population")
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"AnalysisResults/{params_list[0]}_{params_list[1]}_{params_list[2]}_{params_list[3]}_{params_list[4]}_{params_list[5]}_{params_list[6]}Graph{self.__iteration_per_step}")
        plt.cla()
    
    def __plot_result_without_bars(self, iterations, prey_counts, predator_counts, params_list):
        plt.scatter(iterations, prey_counts, color = "blue", label = "Prey population")
        plt.scatter(iterations, predator_counts, color = "red", label = "Predator population")
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"AnalysisResults/{params_list[0]}_{params_list[1]}_{params_list[2]}_{params_list[3]}_{params_list[4]}_{params_list[5]}_{params_list[6]}Graph{self.__iteration_per_step}")
        plt.cla()

