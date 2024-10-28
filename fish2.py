import random


class Fish(Grid):

    def __init__(self, x_coordinate:int, y_coordinate:int) -> None:
        super().__init__(self, width, height, x_coordinate, y_coordinate, Reproductiontime)


    def move(self, list_of_fish, list_of_shark):
        
        list_of_possible_positions = [((self.x_coordinate +1),(self.y_coordinate+1)),((self.x_coordinate+1),(self.y_coordinate-1)),((self.x_coordinate-1),(self.y_coordinate-1)),((self.x_coordinate-1),(self.y_coordinate+1))]
        
        list_positions_fish = [(fish.x_coordinate, fish.y_coordinate) for fish in list_of_fish]

        list_positions_shark = [(shark.x_coordinate, shark.y_coordinate) for shark in list_of_shark] 
        
      


        for element in list_of_possible_positions:
             
            if element in list_positions_fish or list_of_shark:

                 list_of_possible_positions.remove(element) 
                 
        if len(list_of_possible_positions) == 0:
            self.x_coordinate = x_coordinate
            self.y_coordinate = y_coordinate

        else:
            random.shuffle(list_of_possible_positions)  
            self.x_coordinate = list_of_possible_positions[0][0]
            self.y_coordinate = list_of_possible_positions[0][1]

.
   

          
        self.reproduction_time+=1