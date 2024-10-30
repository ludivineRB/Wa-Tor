import random
from Grid import Grid


class Fish(Grid):

    def __init__(self, width, height, x_coordinate:int, y_coordinate:int, reproduction_time: int) -> None:
        self.width = width
        self.height = height
        self.reproduction_time = reproduction_time
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate


    def move(self, list_positions_fish, list_positions_shark, tmp_positions_babyshark, tmp_positions_babyfish):
        
        list_of_possible_positions = [
            super().position(self.x_coordinate, self.y_coordinate+1),
            super().position((self.x_coordinate),(self.y_coordinate-1)),
            super().position((self.x_coordinate-1),(self.y_coordinate)),
            super().position((self.x_coordinate+1),(self.y_coordinate))
            ]


        s1 = set(list_of_possible_positions)
        s2 = set(list_positions_fish)
        s3 = set(list_positions_shark)
        s4 = set(tmp_positions_babyshark)
        s5 = set(tmp_positions_babyfish)
        u1 = s1 & s2
        u2 = s1 & s3
        u3 = s1 & s4
        u4 = s1 & s5
        test = s1-u1
        test2 = s1-u2
        test3 = s1 - u3
        test4 = s1 - u4
        list_of_possible_positions = list(test & test2 & test3 & test4)
        
        # for element in list_of_possible_positions:
        #     if element in u1:
        #             l

        #     if element in u2:
        #             list_of_possible_positions.remove(element)
        # print(list_of_possible_positions)
        # print(list_of_possible_positions)   

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
