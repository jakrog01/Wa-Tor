from Animals.AbstractAnimal import AbstractAnimal
from random import randint

class Prey(AbstractAnimal):
    def __init__(self, x, y, a):
        super().__init__(x, y)
        self.a = a

    def move(self, area):
        pass