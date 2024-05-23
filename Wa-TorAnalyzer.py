from AnalysisScripts.Strategies.PlotOscilationsStrategy import PlotOscilationInTimeStrategy
from AnalysisScripts.Strategies.RespectToStrategies.RespectToBStrategy import RespectToBStrategy
from AnalysisScripts.Strategies.RespectToStrategies.RespectToAreaSizeStrategy import RespectToAreaSizeStrategy
from AnalysisScripts.Strategies.RespectToStrategies.RespectToPreyInitStrategy import RespectToPreyInitStrategy
from AnalysisScripts.Strategies.RespectToStrategies.RespectToPredatorsInitStrategy import RespectToPredatorsInitStrategy

if __name__ == '__main__':
    threads_count = 5
    count_to_average = 2
    iteration_per_step = 1000

    strategy = RespectToPredatorsInitStrategy(False, threads_count, count_to_average, iteration_per_step)

    area_sizes_tuple = set([25])
    init_prey_populations_tuple = set([61])
    init_predators_populations_tuple = set([25,39,30,20,10])
    a_params_tuple = set([5])
    b_params_tuple = set([100])
    c_params_tuple = set([3])
    d_params_tuple = set([7])

    strategy.start_analysis(area_sizes_tuple, init_prey_populations_tuple, init_predators_populations_tuple, a_params_tuple,
                            b_params_tuple, c_params_tuple, d_params_tuple)

    
