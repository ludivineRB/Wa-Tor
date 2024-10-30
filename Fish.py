import random
from Grid import Grid


class Fish(Grid):

    def __init__(self, width, height, x_coordinate:int, y_coordinate:int, reproduction_time: int) -> None:
        self.width = width
        self.height = height
        self.reproduction_time = reproduction_time
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate


    def move(self, list_positions_fish, list_positions_shark):
        
        list_of_possible_positions = [
            super().position(self.x_coordinate, self.y_coordinate+1),
            super().position((self.x_coordinate),(self.y_coordinate-1)),
            super().position((self.x_coordinate-1),(self.y_coordinate)),
            super().position((self.x_coordinate+1),(self.y_coordinate))
            ]


        s1 = set(list_of_possible_positions)
        s2 = set(list_positions_fish)
        s3 = set(list_positions_shark)
        u1 = s1 & s2
        u2 = s1 & s3
        test = s1-u1
        test2 = s1-u2
        list_of_possible_positions = list(test & test2)
     

        if len(list_of_possible_positions) == 0:
            self.x_coordinate = self.x_coordinate
            self.y_coordinate = self.y_coordinate
            self.reproduction_time+=1
        else:
            random.shuffle(list_of_possible_positions)  
            self.x_coordinate = list_of_possible_positions[0][0]
            self.y_coordinate = list_of_possible_positions[0][1]
            #self.x_coordinate, self.y_coordinate = super().position(self.x_coordinate +1, self.y_coordinate)
            self.reproduction_time+=1
