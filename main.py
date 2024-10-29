import Grid
from Fish import Fish
from class_shark import Shark
import random
import os
import time 

height = 10
width = 10

#initialize number of animals
number_of_sharks = 12
number_of_fish = 40
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

count = 0
#infinite loop that will print to console 1 for fish 2 for shark and 0 for nothing
while len(list_of_fish) != 0 and len(list_of_sharks) != 0:
    print_world(list_positions_fish, list_positions_shark)
    l = []
    q = []
    for fish in list_of_fish:
        x_old = fish.x_coordinate
        y_old = fish.y_coordinate
        fish.move(list_positions_fish, list_positions_shark)
        if fish.reproduction_time > 6 and fish.x_coordinate != x_old and fish.y_coordinate != y_old:
            list_of_fish.append(fish(height, width, x_old,y_old))
            l.append((x_old, y_old))
            fish.reproduction_time = 0
        l.append((fish.x_coordinate, fish.y_coordinate))
    list_positions_fish = l

    for shark in list_of_sharks:
        x_old = shark.x_coordinate
        y_old = shark.y_coordinate
        shark.move(list_of_fish, list_of_sharks)
        
        if shark.starvation_time == 0:
            list_of_sharks.remove(shark)

        q.append((shark.x_coordinate, shark.y_coordinate))

    list_positions_shark = q
    list_of_positions_shared = list(set(list_positions_fish) & set(list_of_sharks))

    for fish in list_of_fish:
        if (fish.x_coordinate, fish.y_coordinate) in list_of_positions_shared:
            list_of_fish.remove(fish)
            list_positions_fish.remove((fish.x_coordinate, fish.y_coordinate))



