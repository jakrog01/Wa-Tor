from Animals.AbstractAnimal import AbstractAnimal
from random import randint

class Prey(AbstractAnimal):
    def __init__(self, area_size, x, y, a):
        super().__init__(x, y)
        self.__area_size = area_size
        self.__steps_counter = 0
        self.__a = a

    def move(self, area, new_prey_set):
        print(self.y, self.x)

        possible_moves = self.__choose_direction(area)
        direction = randint(0, len(possible_moves)-1)
        move = possible_moves[direction]

        area[self.y][self.x] = 0

        if move != (0,0):
            if self.__propagation():
                area[self.y][self.x] = 1
                new_prey_set.add(Prey(self.__area_size, self.x, self.y, self.__a))

        self.y = self.__norm_to_boarders(self.y, move[0])
        self.x = self.__norm_to_boarders(self.x, move[1])
        area[self.y][self.x] = 1

    def __propagation(self):
        self.__steps_counter += 1

        if self.__steps_counter >= self.__a:
            print("TAK")
            self.__steps_counter = 0
            return True
        return False

    def __choose_direction(self, area):
        directions = []

        if area[self.__norm_to_boarders(self.y, 1)][self.x] == 0:
            directions.append((1,0))
        
        if area[self.__norm_to_boarders(self.y, -1)][self.x] == 0:
            directions.append((-1,0))
        
        if area[self.y][self.__norm_to_boarders(self.x,1)] == 0:
            directions.append((0,1))
        
        if area[self.y][self.__norm_to_boarders(self.x,-1)] == 0:
            directions.append((0,-1))
        
        if len(directions) != 0:
            return directions
        else:
            return [(0,0)]
    
    def __norm_to_boarders(self, value, step):
        result = value + step
        if result >= self.__area_size:
            return result - self.__area_size
        elif result < 0:
            return result + self.__area_size
        else:
            return result

        