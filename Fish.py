import random
from Grid import Grid


class Fish(Grid):

    def __init__(self, width:int, height:int, x_coordinate:int, y_coordinate:int, reproduction_time: int, age: int, nb_descendants: int, distance) -> None:
        """_summary_ creation of the class Fish

        Args:
            width (int): _description_ int
            height (int): _description_ int
            x_coordinate (int): _description_ int
            y_coordinate (int): _description_ int
            reproduction_time (int): _description_ int
        """
        self.width = width
        self.height = height
        self.reproduction_time = reproduction_time
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.age = age
        self.nb_descendants = nb_descendants
        self.distance = distance


    def move(self, list_positions_fish:list[tuple[int,int]], list_positions_shark:list[tuple[int,int]], tmp_positions_babyshark:list[tuple[int,int]], tmp_positions_babyfish:list[tuple[int,int]])->None:
        """_summary_ move fish and add + 1 to the reproduction_time variable

        Args:
            list_positions_fish (list[tuple[int,int]]): _description_ list of the positions of each object Fish at the start of the loop
            list_positions_shark (list[tuple[int,int]]): _description_ list of the positions of each object Shark at the start of the loop
            tmp_positions_babyshark (list[tuple[int,int]]): _description_ list of the positions of each object babyshark
            tmp_positions_babyfish (list[tuple[int,int]]): _description_ list of the positions of each object babyfish
        Return: None
        """
        
        list_of_possible_positions = [
            super().position(self.x_coordinate, self.y_coordinate+1),
            super().position((self.x_coordinate),(self.y_coordinate-1)),
            super().position((self.x_coordinate-1),(self.y_coordinate)),
            super().position((self.x_coordinate+1),(self.y_coordinate))
            ]

        #Exclusion of positions occupied by other objects
        set_of_possible_positions= set(list_of_possible_positions)
        set_of_fish_positions = set(list_positions_fish)
        set_of_sharks_positions = set(list_positions_shark)
        set_of_babyshark_positions = set(tmp_positions_babyshark)
        set_of_babyfish_positions = set(tmp_positions_babyfish)

        possible_positions_without_fish = set_of_possible_positions-set_of_fish_positions
        possible_positions_without_sharks= set_of_possible_positions-set_of_sharks_positions
        possible_positions_without_babysharks = set_of_possible_positions - set_of_babyshark_positions
        possible_positions_without_babyfish = set_of_possible_positions- set_of_babyfish_positions
        list_of_possible_positions = list(possible_positions_without_fish & possible_positions_without_sharks & possible_positions_without_babysharks & possible_positions_without_babyfish)

        if len(list_of_possible_positions) == 0:
            self.x_coordinate = self.x_coordinate
            self.y_coordinate = self.y_coordinate
            self.reproduction_time+=1
        else:
            random.shuffle(list_of_possible_positions)  
            self.x_coordinate = list_of_possible_positions[0][0]
            self.y_coordinate = list_of_possible_positions[0][1]
            self.reproduction_time+=1