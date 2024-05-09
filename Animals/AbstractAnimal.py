from abc import ABC, abstractmethod

class AbstractAnimal(ABC):
    def __init__(self, x, y):
        super().__init__()
        self.y = y
        self.x = x
    
    @abstractmethod
    def move(self):
        pass