from grid import position

class Shark(Fish):
    def __init__(self, width:int, height:int, x_coordinate:int, y_coordinate:int, reproduction_time:int, starvation_time:int):
        super().__init__(width, height, x_coordinate, y_coordinate, reproduction_time)
        self.starvation_time = starvation_time
        

    def move(self):
        """_summary_ : Change of the x and y position for each object in Shark class. 
        """
        list_of_possible_positions = [(position((self.x_coordinate +1),(self.y_coordinate+1))),(position((self.x_coordinate+1),(self.y_coordinate-1))),(position((self.x_coordinate-1),(self.y_coordinate-1))),(position((self.x_coordinate-1),(self.y_coordinate+1)))]
        
        #Creation d'une liste de position de tous les poissons
        list_positions_fish = []
        #récupération des positions des poissons. List_of_fish contient les positions de tous les poissons
        for fish in list_of_fish:
            list_positions_fish.append((fish.x_coordinate, fish.y_coordinate))
        #comparaison position poissons, positions shark
        for pos in range(len(list_of_possible_positions)):
            if list_of_possible_positions[pos] in list_positions_fish: #il faut prendre juste les coordonnées de l'objet fish...
                self.starvation_time = 3
                list_of_fish.pop(pos)
                #déplacement du requin
                self.x_position=list_positions_fish[pos].x_coordinate
                self.y_position=list_positions_fish[pos].y_coordinate
            else :
                self.starvation_time-=1
                #déplacement
                super().move(self)

        if self.starvation_time == 0:
                list_of_sharks.pop(self)

        self.reproduction_time+=1
        