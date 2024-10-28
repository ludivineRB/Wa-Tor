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

        for element in list_of_possible_positions:
            if element in list_positions_fish:
                self.starvation_time = 3
                self.x_coordinate = element[0]
                self.y_coordinate = element[1]

        if len(l) == 0:
            self.starvation_time -= 1
            super().move(list_positions_fish, list_positions_shark)
        #comparaison position poissons, positions shark
        # for pos in range(len(list_of_possible_positions)):
        #     if list_of_possible_positions[pos] in list_positions_fish: #il faut prendre juste les coordonnées de l'objet fish...
        #         self.starvation_time = 3
        #         list_positions_fish.remove(pos)
        #         #déplacement du requin
        #         self.x_coordinate=list_positions_fish[pos].x_coordinate
        #         self.y_coordinate=list_positions_fish[pos].y_coordinate
        #     else :
        #         self.starvation_time-=1
        #         #déplacement
        #         super().move(list_positions_fish, list_positions_shark)


        self.reproduction_time+=1
        