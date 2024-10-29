from Grid import Grid
from Fish import Fish

class Shark(Fish):
    def __init__(self, width:int, height:int, x_coordinate:int, y_coordinate:int, reproduction_time:int, starvation_time:int):
        super().__init__(width, height, x_coordinate, y_coordinate, reproduction_time)
        self.starvation_time = starvation_time
        

    def move(self, list_positions_fish, list_positions_shark):
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
            self.starvation_time = 3

        else:
            self.starvation_time -= 1
            super().move(list_positions_fish, list_positions_shark)
        
        self.reproduction_time+=1
        