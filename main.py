import Grid
from Fish import Fish
from class_shark import Shark
import random
import os
import time 
from data import get_data

height = 5
width = 5

#initialize number of animals
number_of_sharks = 1
number_of_fish = 15
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
    list_of_sharks.append(Shark(width,height,shark[0],shark[1],0, 3))


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
    get_data(chronon, number_of_fish,number_of_sharks)

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
    time.sleep(0.5) 

chronon = 0

#infinite loop that will print to console 1 for fish 2 for shark and 0 for nothing
while len(list_of_fish) != 0  and len(list_of_sharks)!=0:
    print_world(list_positions_fish, list_positions_shark)
    #l list positions fish
    l = []
    #q list positions shark
    q = []
    #boucles pour move les fish mise à jour l
    for i in range(len(list_of_fish)):
        x_old = list_of_fish[i].x_coordinate
        y_old = list_of_fish[i].y_coordinate

        list_of_fish[i].move(list_positions_fish, list_positions_shark)
        #ajout des nouvelles coordonnées de poissons à la liste l    
        l.append((list_of_fish[i].x_coordinate, list_of_fish[i].y_coordinate))
        list_positions_fish[i] = (list_of_fish[i].x_coordinate, list_of_fish[i].y_coordinate)
        #reproduction time si possible 
        if list_of_fish[i].reproduction_time > 6 and [list_of_fish[i].x_coordinate != x_old and list_of_fish[i].y_coordinate != y_old]:
            list_of_fish.append(Fish(height, width, x_old,y_old, 0))
            l.append((x_old, y_old))
            list_of_fish[i].reproduction_time = 0
        
    list_positions_fish = l

    #boucles pour move les sharks
    for j in range(len(list_of_sharks)):
        x_old = list_of_sharks[j].x_coordinate
        y_old = list_of_sharks[j].y_coordinate
        list_of_sharks[j].move(list_positions_fish, list_positions_shark)
        
        #vérifier le starving des requins
        if list_of_sharks[j].starvation_time == 0:
            list_of_sharks[j].x_coordinate = "a"
            list_of_sharks[j].y_coordinate = "a"

        if list_of_sharks[j].x_coordinate != "a":
            q.append((list_of_sharks[j].x_coordinate, list_of_sharks[j].y_coordinate))
            list_positions_shark[j] =(list_of_sharks[j].x_coordinate, list_of_sharks[j].y_coordinate)
        
        #add reproduction for sharks
        if list_of_sharks[j].reproduction_time > 6 and [list_of_sharks[j].x_coordinate != x_old and list_of_sharks[j].y_coordinate != y_old]:
            list_of_sharks.append(Shark(height, width, x_old,y_old, 0,3))
            q.append((x_old, y_old))
            list_of_sharks[j].reproduction_time = 0
        
    list_positions_shark = q
    print(f"liste de positions de requins {list_positions_shark}")
    #Creation liste de position partagée
    list_of_positions_shared = list(set(list_positions_fish) & set(list_positions_shark))

    tmplistcoord = []
    tmplistfish = []
    #kill fish in the same position of shark
    for fish in list_of_fish:
        if (fish.x_coordinate,fish.y_coordinate) not in list_of_positions_shared:
            tmplistcoord.append((fish.x_coordinate,fish.y_coordinate))
            tmplistfish.append(fish)
            
            
    
    #print(list_positions_fish)
   
    #print(list_positions_shark)
    list_positions_fish = tmplistcoord
    list_of_fish = tmplistfish
    #print(f"liste de positions {list_positions_fish}")

    #comptage chronon, fish and sharks
    chronon += 1
    #number_of_fish = len(list_of_fish)
    #number_of_sharks = len(list_of_sharks)

    print(chronon)
    