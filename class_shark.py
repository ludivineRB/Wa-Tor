from Grid import Grid
from Fish import Fish
import random
class Shark(Fish):
    def __init__(self, width:int, height:int, x_coordinate:int, y_coordinate:int, reproduction_time:int, starvation_time:int):
        super().__init__(width, height, x_coordinate, y_coordinate, reproduction_time)
        self.starvation_time = starvation_time
        

    def move(self, list_positions_fish, list_positions_shark, tmp_positions_babyshark):
        """_summary_ : Change of the x and y position for each object in Shark class. 
        """
        list_of_possible_positions = [
            super().position(self.x_coordinate , self.y_coordinate+1),
            super().position((self.x_coordinate),(self.y_coordinate-1)),
            super().position((self.x_coordinate-1),(self.y_coordinate)),
            super().position((self.x_coordinate+1),(self.y_coordinate))
            ]

        l= list(set(list_positions_fish) & set(list_of_possible_positions))
       
        if len(l)>0: 
            self.x_coordinate = l[0][0]
            self.y_coordinate = l[0][1]
            self.starvation_time = 9
        

        else:
            self.starvation_time-=1
            s1 = set(list_of_possible_positions)
            s3 = set(list_positions_shark)
            s4 = set(tmp_positions_babyshark)
            u2 = s1 & s3
            u3 = s1 & s4
            test2 = s1-u2
            test3 = s1-u3
            list_of_possible_positions = list(test2 & test3)
            if len(list_of_possible_positions) == 0:
                self.x_coordinate = self.x_coordinate
                self.y_coordinate = self.y_coordinate
            else:
                random.shuffle(list_of_possible_positions)  
                self.x_coordinate = list_of_possible_positions[0][0]
                self.y_coordinate = list_of_possible_positions[0][1]
                #self.x_coordinate, self.y_coordinate = super().position(self.x_coordinate +1, self.y_coordinate)
        self.reproduction_time+=1
        