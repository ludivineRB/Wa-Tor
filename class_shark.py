class Shark(Fish):
    def __init__(self, width:int, height:int, x_coordinate:int, y_coordinate:int, reproduction_time:int, starvation_time:int):
        #position defined by a tuple in grid class
        super().__init__(width, height, x_coordinate, y_coordinate, reproduction_time)
        self.starvation_time = starvation_time
        

    def moove(self):
        """return super().moove()
            pass
            """

    
    def starvation(self):

        list_of_coordinates = [] #liste de toutes les coordonnées du monde
        list_of_sharks = [] #liste de objets requins
        list_of_fish = [] #liste de objets fish

        list_of_possible_positions = [((self.x_coordinate +1),(self.y_coordinate+1)),((self.x_coordinate+1),(self.y_coordinate-1)),((self.x_coordinate-1),(self.y_coordinate-1)),((self.x_coordinate-1),(self.y_coordinate+1))]
        
        #Creation d'une liste de position de tous les poissons
        list_positions_fish = []
        #récupération des positions des poissons
        for fish in list_of_fish:
            list_positions_fish.append((fish.x_coordinate, fish.y_coordinate))
        #comparaison position poissons, positions shark
        for position in range(len(list_of_possible_positions)):
            if list_of_possible_positions[position] in list_positions_fish: #il faut prendre juste les coordonnées de l'objet fish...
                self.starvation_time = 3
                list_of_fish.pop(position)
                #déplacement du requin
                self.x_position=list_positions_fish[position].x_coordinate
                self.y_position=list_positions_fish[position].y_coordinate
            else :
                self.starvation_time-=1
                #déplacement
                ##récupération du move()de fish
        if self.starvation_time == 0:
                list_of_sharks.pop(self)

        self.reproduction_time+=1
        