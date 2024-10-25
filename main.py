# import grid
# import fish
# import shark
import random

height = 5
width = 5

#initialize number of animals
number_of_sharks = 4
number_of_fish = 8
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
    # list_of_sharks.append(shark(width,height,shark[0],shark[1]))
    print(shark[0],shark[1])

for fish in list_of_random_coordinates[number_of_sharks:]:
    # list_of_fish.append(fish(width,height,fish[0],fish[1]))
    print(fish[0],fish[1])

#create function to print the simulation onto the console
def print_world() -> None:
    """
        print to console positions of fish and shark

        args
        none
        
        returns
        none
    """
    for y in height:
        row = ""
        for x in width:
            if x == fish.x_coordinate and y == fish.y_coordinate:
                row += "1"

            elif x == shark.x_coordinate and y == shark.y_coordinate:
                row += "2"
            
            else:
                row += "0"
        print(row)
        
#infinite loop that will print to console 1 for fish 2 for shark and 0 for nothing
# while len(list_of_fish) != 0 and len(list_of_sharks) != 0:

#     print_world()

#     for fish in list_of_fish:
#         fish.move()

#     for shark in list_of_sharks:
#         shark.move()
