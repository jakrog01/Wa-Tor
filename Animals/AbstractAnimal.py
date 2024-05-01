from abc import ABC, abstractmethod

class AbstractAnimal(ABC):
    def __init__(self):
        super().__init__()
        self.y = 0
        self.x = 0
        self.next_move = 0
    
    @abstractmethod
    def move(self):
        pass