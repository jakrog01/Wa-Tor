from Animals.AbstractAnimal import AbstractAnimal

class Predator(AbstractAnimal):
    def __init__(self, x, y, b, c, d):
        super().__init__(x,y)
        self.b = b
        self.c = c
        self.d = d

    def move(self, area):
        pass