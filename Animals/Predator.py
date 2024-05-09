from Animals.AbstractAnimal import AbstractAnimal
from Animals.Prey import Prey
from random import randint

class Predator(AbstractAnimal):
    def __init__(self, x, y, area_size, b, c, d):
        super().__init__(x,y)
        self.__area_size = area_size
        self.__death_counter = 0
        self.__steps_counter = 0
        self.__b = b
        self.__c = c
        self.__d = d

    def movement(self, area, new_predator_set, delete_predator_set, delete_prey_set):
        directions = self.__choose_direction(area)
        possible_moves = directions[0] 
        next_move_value = directions[1]

        direction = randint(0, len(possible_moves)-1)
        move = possible_moves[direction]

        area[self.y][self.x] = 0

        if next_move_value == 0:
            if move != (0,0):
                if self.__death():
                    area[self.y][self.x] = 0
                    delete_predator_set.add(self)
                elif self.__propagation():
                    area[self.y][self.x] = 2
                    new_predator_set.add(Predator(self.x, self.y, self.__area_size, self.__b, self.__c, self.__d))
            
        elif next_move_value == 1:
            if randint(1,100) <= self.__b:
                self.__death_counter = 0
                delete_prey_set.add(Prey(0 ,self.__norm_to_boarders(self.x, move[1]), self.__norm_to_boarders(self.y, move[0]), 0))
                if self.__propagation():
                    area[self.y][self.x] = 2
                    new_predator_set.add(Predator(self.x, self.y, self.__area_size, self.__b, self.__c, self.__d))
            else:
                self.move = (0,0)
                if self.__death():
                    area[self.y][self.x] = 0
                    delete_predator_set.add(self)

        if self not in delete_predator_set:
            self.y = self.__norm_to_boarders(self.y, move[0])
            self.x = self.__norm_to_boarders(self.x, move[1])
            area[self.y][self.x] = 2

    def __propagation(self):
        self.__steps_counter += 1

        if self.__steps_counter >= self.__d:
            self.__steps_counter = 0
            return True
        return False
    
    def __death(self):
        self.__death_counter += 1
        if self.__death_counter >= self.__c:
            return True
        return False

    def __choose_direction(self, area):
        directions = self.__find_path(area, 1)
        if directions[0] == [(0,0)]:
            directions = self.__find_path(area, 0)
        return directions
        
    def __find_path(self, area, value):
        directions = []

        if area[self.__norm_to_boarders(self.y, 1)][self.x] == value:
            directions.append((1,0))
        
        if area[self.__norm_to_boarders(self.y, -1)][self.x] == value:
            directions.append((-1,0))
        
        if area[self.y][self.__norm_to_boarders(self.x,1)] == value:
            directions.append((0,1))
        
        if area[self.y][self.__norm_to_boarders(self.x,-1)] == value:
            directions.append((0,-1))
        
        if len(directions) != 0:
            return [directions,value]
        else:
            return [[(0,0)], value]
        
    def __norm_to_boarders(self, value, step):
        result = value + step
        if result >= self.__area_size:
            return result - self.__area_size
        elif result < 0:
            return result + self.__area_size
        else:
            return result