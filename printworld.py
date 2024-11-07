import time
import os

def print_world(list_positions_fish:list[tuple[int,int]], list_positions_shark:list[tuple[int,int]], height:int, width:int) -> None:
    """_summary_ print in console the world with the positions of each objects (fish and shark)

    Args:
        list_positions_fish (list[tuple[int,int]]): _description_ list of tuples with each position of fish object
        list_positions_shark (list[tuple[int,int]]): _description_ list of tuples with each position of shark object
        height (int): height of the grid
        width (int): width of the grid
    """
    
    os.system("clear")
    print(end="")
    world_display=""
    for y in range(height):
        row = ""
        for x in range(width):
            if (x,y) in list_positions_fish:
                row += f"\U0001F420" + "|"
            elif (x,y) in list_positions_shark:
                row += f"\U0001F988" + "|"
            else:
                row += f"\U0001F30A" + "|"
            row+=""
        world_display += row + "\n"
        
    print(world_display)
    time.sleep(0.01) 