from abc import ABC, abstractmethod

class AbstractRespectToStrategy():
    def __init__(self):
        pass
    
    @abstractmethod
    def start_analysis(self):
        pass