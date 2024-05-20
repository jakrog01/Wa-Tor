from abc import ABC, abstractmethod

class RespectToBStrategy():
    def __init__(self):
        pass
    
    @abstractmethod
    def start_analysis(self):
        pass