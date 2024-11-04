from Grid import Grid
from Fish import Fish
import random

class Shark(Fish):
    def __init__(self, width:int, height:int, x_coordinate:int, y_coordinate:int, reproduction_time:int, starvation_time:int)->None:
        """_summary_ creation of the class Shark

        Args:
            width (int): _description_ int
            height (int): _description_ int
            x_coordinate (int): _description_ int
            y_coordinate (int): _description_ int
            reproduction_time (int): _description_ int
            starvation_time (int): _description_ int
        """
        super().__init__(width, height, x_coordinate, y_coordinate, reproduction_time)
        self.starvation_time = starvation_time
        

    def move(self, list_positions_fish:list[tuple[int,int]], list_positions_shark:list[tuple[int,int]], tmp_positions_babyshark:list[tuple[int,int]])->None:
        """_summary_ move shark, add + 1 to the reproduction_time variable and add 4 to the variable starvation_time if it eats a fish 

        Args:
            list_positions_fish (list[tuple[int,int]]): _description_ list of the positions of each object Fish at the start of the loop
            list_positions_shark (list[tuple[int,int]]): _description_ list of the positions of each object Shark at the start of the loop
            tmp_positions_babyshark (list[tuple[int,int]]): _description_ list of the positions of each object babyshark
        Return: None
        """ 

        list_of_possible_positions = [
            super().position(self.x_coordinate , self.y_coordinate+1),
            super().position((self.x_coordinate),(self.y_coordinate-1)),
            super().position((self.x_coordinate-1),(self.y_coordinate)),
            super().position((self.x_coordinate+1),(self.y_coordinate))
            ]

        list_of_possible_positions_without_fish= list(set(list_positions_fish) & set(list_of_possible_positions))
       
        if len(list_of_possible_positions_without_fish)>0: 
            self.x_coordinate = list_of_possible_positions_without_fish[0][0]
            self.y_coordinate = list_of_possible_positions_without_fish[0][1]
            self.starvation_time = 3
        

        else:
            self.starvation_time-=1

            #Exclusion of positions occupied by other objects
            set_of_possible_positions= set(list_of_possible_positions)
            set_of_fish_positions = set(list_positions_fish)
            set_of_sharks_positions = set(list_positions_shark)
            set_of_babyshark_positions = set(tmp_positions_babyshark)

            intersection_possible_and_fish_positions = set_of_possible_positions & set_of_fish_positions
            intersection_possible_and_sharks_positions = set_of_possible_positions & set_of_sharks_positions
            intersection_possible_and_babyshark_positions = set_of_possible_positions & set_of_babyshark_positions

            possible_positions_without_fish = set_of_possible_positions-intersection_possible_and_fish_positions
            possible_positions_without_sharks= set_of_possible_positions-intersection_possible_and_sharks_positions
            possible_positions_without_babysharks = set_of_possible_positions - intersection_possible_and_babyshark_positions
            list_of_possible_positions = list(possible_positions_without_fish & possible_positions_without_sharks & possible_positions_without_babysharks)

            if len(list_of_possible_positions) == 0:
                self.x_coordinate = self.x_coordinate
                self.y_coordinate = self.y_coordinate
            else:
                #random.shuffle(list_of_possible_positions)  
                self.x_coordinate = list_of_possible_positions[0][0]
                self.y_coordinate = list_of_possible_positions[0][1]
        self.reproduction_time+=1
        