import random
from Fish import Fish
from class_shark import Shark

def list_creation(height:int, width:int, number_of_sharks:int, number_of_animals:int)->tuple:
    """_summary_ initializes Fish and Shark object

    Args:
        height (int): _description_ height of the Grid
        width (int): _description_ width of the Grid
        number_of_sharks (int): _description_
        number_of_animals (int): _description_

    Returns:
        tuple: _description_ a list of objects Fish, a list of objects Sharks, a list of tuples of fish coordinates, a list of tuples of sharks coordinates
    """
    #initialize objects
    list_of_coordinates = []
    list_of_sharks = []
    list_of_fish = []
    #create coordinates of the grid
    for y in range(height):
        for x in range(width):
            list_of_coordinates.append((x,y))
    #create random coordinates for animals
    list_of_random_coordinates = random.sample(list_of_coordinates, number_of_animals)

    for shark in list_of_random_coordinates[:number_of_sharks]:
        list_of_sharks.append(Shark(width, height, shark[0], shark[1], 0, 2, 0, 0, 0))

    for fish in list_of_random_coordinates[number_of_sharks:]:
        list_of_fish.append(Fish(width, height, fish[0], fish[1], 0, 0, 0, 0))

    list_positions_fish = [(fish.x_coordinate, fish.y_coordinate) for fish in list_of_fish]
    list_positions_shark = [(shark.x_coordinate, shark.y_coordinate) for shark in list_of_sharks]

    return list_of_fish, list_of_sharks, list_positions_fish, list_positions_shark