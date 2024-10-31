import Grid
from Fish import Fish
from class_shark import Shark
import random
import os
import time 
from data import get_data

height = 10
width = 10

#initialize number of animals
number_of_sharks = 1
number_of_fish = 25
number_of_animals = number_of_sharks + number_of_fish

#initialize objects
list_of_coordinates = []
list_of_sharks = []
list_of_fish = []
list_of_animals = []

for y in range(height):
    for x in range(width):
        list_of_coordinates.append((x,y))

#create random coordinates for animals
#create list of fish and sharks
list_of_random_coordinates = random.sample(list_of_coordinates, number_of_animals)

for shark in list_of_random_coordinates[:number_of_sharks]:
    list_of_sharks.append(Shark(width,height,shark[0],shark[1],0, 10))


for fish in list_of_random_coordinates[number_of_sharks:]:
    list_of_fish.append(Fish(width,height,fish[0],fish[1],0))

list_positions_fish = [(fish.x_coordinate, fish.y_coordinate) for fish in list_of_fish]
list_positions_shark = [(shark.x_coordinate, shark.y_coordinate) for shark in list_of_sharks] 

#create function to print the simulation onto the console
def print_world(list_positions_fish, list_positions_shark) -> None:
    """
        print to console positions of fish and shark

        args
        none
        
        returns
        none
    """
    #get_data(chronon, number_of_fish,number_of_sharks)

    os.system("clear")
    print("\033[H", end="")
   
    for y in range(height):
        row = ""
        for x in range(width):
            if (x,y) in list_positions_fish:
                row += " ~ "

            elif (x,y) in list_positions_shark:
                row += " O "
            
            else:
                row += " . "
        print(row)
    time.sleep(0.1) 

chronon = 0

#infinite loop that will print to console 1 for fish 2 for shark and 0 for nothing
while len(list_of_fish) != 0 and len(list_of_sharks)!=0:
    print_world(list_positions_fish, list_positions_shark)
    temp_list_positions_fish = []
    temp_list_positions_shark = []
    temp_list_of_fish = []
    temp_list_of_shark = []
    temp_positions_babyshark = []
    temp_positions_babyfish = []
    list_of_shared_positions= [] 
    
    #boucles pour move les sharks
    for j in range(len(list_of_sharks)):
        x_old = list_of_sharks[j].x_coordinate
        y_old = list_of_sharks[j].y_coordinate
        list_of_sharks[j].move(list_positions_fish, list_positions_shark, temp_positions_babyshark)
        
        #vérifier le starving des requins
        if list_of_sharks[j].starvation_time == 0:
            pass
        else:
            temp_list_positions_shark.append((list_of_sharks[j].x_coordinate, list_of_sharks[j].y_coordinate))
            temp_list_of_shark.append(list_of_sharks[j])
            list_positions_shark[j] =(list_of_sharks[j].x_coordinate, list_of_sharks[j].y_coordinate)
            #add reproduction for sharks
            if list_of_sharks[j].reproduction_time > 3:
                if list_of_sharks[j].x_coordinate != x_old or list_of_sharks[j].y_coordinate != y_old:
                    temp_list_of_shark.append(Shark(height, width, x_old,y_old, 0,8))
                    temp_list_positions_shark.append((x_old, y_old))
                    list_of_sharks[j].reproduction_time = 0
                    temp_positions_babyshark.append((x_old,y_old))


            #creation de liste =q
            if list_of_sharks[j].starvation_time==9:
                list_of_shared_positions.append((list_of_sharks[j].x_coordinate, list_of_sharks[j].y_coordinate))

    #boucles pour move les fish mise à jour l
    for i in range(len(list_of_fish)):
        if (list_of_fish[i].x_coordinate, list_of_fish[i].y_coordinate) in list_of_shared_positions:      
            pass

        else:
            x_old = list_of_fish[i].x_coordinate
            y_old = list_of_fish[i].y_coordinate

            list_of_fish[i].move(list_positions_fish, list_positions_shark, temp_positions_babyshark, temp_positions_babyfish)
            #ajout des nouvelles coordonnées de poissons à la liste l    
            temp_list_positions_fish.append((list_of_fish[i].x_coordinate, list_of_fish[i].y_coordinate))
            list_positions_fish[i] = (list_of_fish[i].x_coordinate, list_of_fish[i].y_coordinate)
            temp_list_of_fish.append(list_of_fish[i])
            #reproduction time si possible
            if list_of_fish[i].reproduction_time > 3:
                if list_of_fish[i].x_coordinate != x_old or list_of_fish[i].y_coordinate != y_old:
                    temp_list_of_fish.append(Fish(height, width, x_old,y_old, 0))
                    temp_list_positions_fish.append((x_old, y_old))
                    list_of_fish[i].reproduction_time = 0
                    temp_positions_babyfish.append((x_old,y_old))

    
    list_positions_shark = temp_list_positions_shark
    list_of_sharks = temp_list_of_shark
    list_of_fish = temp_list_of_fish   
    list_positions_fish = temp_list_positions_fish
    chronon += 1
