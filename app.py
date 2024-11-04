import Grid
from Fish import Fish
from class_shark import Shark
import random
import os
import time
import pygame 
import sys

  
# initializing the constructor 
pygame.init() 
  
# initialize screen
res = (1920,1080) 
screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()

# FPS (frames per second) controller
fps = pygame.time.Clock()

# initalize colours
white = (255,255,255) 
color_light = (170,170,170) 
color_dark = (100,100,100)   
screen.fill((51,255,255))
black = (0,0,0)
blue = (51,255,255)
grey = (100,100,100)
red = (255,0,0)
blue_grid = (204,229,255)

#initalize dimensions
screen_width = screen.get_width() 
screen_height = screen.get_height()
ocean_waves = pygame.image.load("ocean-waves.jpg") 
ocean_waves = pygame.transform.scale(ocean_waves,res)
screen.blit(ocean_waves, (0,0))
  
# creating text for buttons
smallfont = pygame.font.SysFont('Corbel',35)
bigfont = pygame.font.SysFont('Corbel',200)
text1 = smallfont.render('start' , True , white)
text2 = smallfont.render('quit' , True , white)
title = bigfont.render('Wa-Tor', True, white)
screen.blit(title, (screen_width/2,screen_height/2))

height = 40
width = 40

#initialize number of animals
number_of_sharks = 25
number_of_fish = 200
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
list_of_random_coordinates = random.sample(list_of_coordinates, number_of_animals)

for shark in list_of_random_coordinates[:number_of_sharks]:
    list_of_sharks.append(Shark(width,height,shark[0],shark[1],0, 2))


for fish in list_of_random_coordinates[number_of_sharks:]:
    list_of_fish.append(Fish(width,height,fish[0],fish[1],0))

list_positions_fish = [(fish.x_coordinate, fish.y_coordinate) for fish in list_of_fish]
list_positions_shark = [(shark.x_coordinate, shark.y_coordinate) for shark in list_of_sharks] 

def drawGrid(list_positions_fish:list[tuple[int,int]], list_positions_shark:list[tuple[int,int]])->None:
    """_summary_ function that draws the world and the animals that live on it

    Args:
        list_positions_fish (list[tuple[int,int]]): _description_ list of tuples with each position of fish object to draw their position in the world
        list_positions_shark (list[tuple[int,int]]): _description_ list of tuples with each position of shark object to draw their position in the world
    """
    #load images
    nemo = pygame.image.load("nemo-removebg-preview.png")
    shark = pygame.image.load("shark-removebg-preview.png")
    ocean = pygame.image.load('ocean.png')
    ocean = pygame.transform.scale(ocean,res)
    screen.blit(ocean, (0,0))
    #create grid dimensions
    block_size = 25
    grid_width = width
    grid_height = height
    for x in range(grid_width):
        for y in range(grid_height):
            rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
            pygame.draw.rect(screen, blue_grid, rect,1)
            if (x,y) in list_positions_fish:
                nemo = pygame.transform.scale(nemo,(25,25))
                screen.blit(nemo,(x*block_size,y*block_size))

            elif (x,y) in list_positions_shark:
                shark = pygame.transform.scale(shark,(25,25))
                screen.blit(shark,(x*block_size,y*block_size))
            
            else:
                pass
                
            pygame.draw.rect(screen, blue_grid, rect,1)


def create_shark_text(list_positions_shark:list[tuple[int,int]])->str:
    """_summary_ return in a string type the number of sharks 

    Args:
        list_positions_shark (list[tuple[int,int]]): _description_ list of tuples with each position of shark object 

    Returns:
        str: _description_ number of sharks 
    """
    text = 'number of shark: ' + str(len(list_positions_shark))
    return text

def create_fish_text(list_positions_fish:list[tuple[int,int]])->str:
    """_summary_ return in a string type the number of fish

    Args:
        list_positions_fish (list[tuple[int,int]]): _description_ list of tuples with each position of fish object

    Returns:
        str: _description_ number of fish
    """
    text = 'number of fish: ' + str(len(list_positions_fish))
    return text

def create_chronon_text(chronon:int)->str:
    """_summary_ return in a string type the number of chronon 

    Args:
        chronon (int): _description_ int

    Returns:
        int: _description_ number of chronon
    """
    text = 'Time elapsed: ' + str(chronon)
    return text



def main_pygame(list_positions_fish:list[tuple[int,int]],list_positions_shark:list[tuple[int,int]], list_of_fish:list[object], list_of_sharks:list[object])->None:
    """_summary_ creates pygame world

    Args:
        list_positions_fish (list[tuple[int,int]]): _description_ list of tuples with each position of fish object 
        list_positions_shark (list[tuple[int,int]]): _description_list of tuples with each position of shark object 
        list_of_fish (list[object]): _description_ list of all fish object
        list_of_sharks (list[object]): _description_ list of all sharks object
    """
    chronon = 0
    while len(list_of_fish) != 0  and len(list_of_sharks)!=-0:
        drawGrid(list_positions_fish, list_positions_shark)
        nb_shark_text = create_shark_text(list_positions_shark)
        shark_text = smallfont.render(nb_shark_text, True, white)
        nb_fish_text = create_fish_text(list_positions_fish)
        fish_text = smallfont.render(nb_fish_text, True, white)
        chronon_text = create_chronon_text(chronon)
        chronon_metre_text = smallfont.render(chronon_text, True, white)

        screen.blit(shark_text, (screen_width-300,screen_height-200))
        screen.blit(fish_text, (screen_width-300,screen_height-160))
        screen.blit(chronon_metre_text, (screen_width-300,screen_height -120))

        temp_list_positions_fish = []
        temp_list_positions_shark = []
        temp_list_of_fish = []
        temp_list_of_shark = []
        temp_positions_babyshark = []
        temp_positions_babyfish = []
        list_of_shared_positions= [] 

        #loop to move sharks
        for j in range(len(list_of_sharks)):
            x_old = list_of_sharks[j].x_coordinate
            y_old = list_of_sharks[j].y_coordinate
            list_of_sharks[j].move(list_positions_fish, list_positions_shark, temp_positions_babyshark)
            
            #checks starvation time of shark
            if list_of_sharks[j].starvation_time == 0:
                pass
            else:
                temp_list_positions_shark.append((list_of_sharks[j].x_coordinate, list_of_sharks[j].y_coordinate))
                temp_list_of_shark.append(list_of_sharks[j])
                list_positions_shark[j] =(list_of_sharks[j].x_coordinate, list_of_sharks[j].y_coordinate)
                #reproduction of sharks
                if list_of_sharks[j].reproduction_time > 6:
                    if list_of_sharks[j].x_coordinate != x_old or list_of_sharks[j].y_coordinate != y_old:
                        temp_list_of_shark.append(Shark(height, width, x_old,y_old, 0,2))
                        temp_list_positions_shark.append((x_old, y_old))
                        list_of_sharks[j].reproduction_time = 0
                        temp_positions_babyshark.append((x_old,y_old))


                #checks if shark eats a fish
                if list_of_sharks[j].starvation_time==3:
                    list_of_shared_positions.append((list_of_sharks[j].x_coordinate, list_of_sharks[j].y_coordinate))

        #loop to move fish
        for i in range(len(list_of_fish)):
            if (list_of_fish[i].x_coordinate, list_of_fish[i].y_coordinate) in list_of_shared_positions:      
                pass

            else:
                x_old = list_of_fish[i].x_coordinate
                y_old = list_of_fish[i].y_coordinate

                list_of_fish[i].move(list_positions_fish, list_positions_shark, temp_positions_babyshark, temp_positions_babyfish)
                #refresh list of fish and list of fish positions 
                temp_list_positions_fish.append((list_of_fish[i].x_coordinate, list_of_fish[i].y_coordinate))
                list_positions_fish[i] = (list_of_fish[i].x_coordinate, list_of_fish[i].y_coordinate)
                temp_list_of_fish.append(list_of_fish[i])
                #reproduction of fish
                if list_of_fish[i].reproduction_time > 1:
                    if list_of_fish[i].x_coordinate != x_old or list_of_fish[i].y_coordinate != y_old:
                        temp_list_of_fish.append(Fish(height, width, x_old,y_old, 0))
                        temp_list_positions_fish.append((x_old, y_old))
                        list_of_fish[i].reproduction_time = 0
                        temp_positions_babyfish.append((x_old,y_old))

        #update list
        list_positions_shark = temp_list_positions_shark
        list_of_sharks = temp_list_of_shark
        list_of_fish = temp_list_of_fish   
        list_positions_fish = temp_list_positions_fish
        chronon += 1

        for ev in pygame.event.get(): 
            
            if ev.type == pygame.QUIT: 
                pygame.quit() 
                
            #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                
                #if the mouse is clicked on the 
                # button the game is terminated 
                if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2 <= mouse[1] <= screen_height/2+40:
                    main_pygame(list_positions_fish,list_positions_shark,list_of_fish, list_of_sharks)

                if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2+40 < mouse[1] <= screen_height/2+140:
                    pygame.quit()
        
        # stores the (x,y) coordinates into the variable as a tuple 
        mouse = pygame.mouse.get_pos() 
        
        pygame.draw.rect(screen,color_dark,[screen_width-200,screen_height/2+40,140,40]) 
        screen.blit(text2 , (screen_width+50-200,screen_height/2+50))

        if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2 <= mouse[1] <= screen_height/2+40: 
            pygame.draw.rect(screen,color_light,[screen_width-200,screen_height/2,140,40])

        #events as in button clicks
        pygame.display.update()
        fps.tick(10)

#infinite loop to run pygame
while True:
    #events as in button clicks
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2 <= mouse[1] <= screen_height/2+40:
                main_pygame(list_positions_fish,list_positions_shark,list_of_fish, list_of_sharks)
                #drawGrid(list_positions_fish,list_positions_shark)

            if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2+40 < mouse[1] <= screen_height/2+140:
                pygame.quit()
                  
    # while mouse_pressed:
    # stores the (x,y) coordinates into the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
    
    #create buttons with text on them and change colour if mouse hovers over them
    pygame.draw.rect(screen,color_dark,[screen_width-200,screen_height/2,140,40]) 
    pygame.draw.rect(screen,color_dark,[screen_width-200,screen_height/2+40,140,40]) 
    screen.blit(text1 , (screen_width+50-200,screen_height/2))
    screen.blit(text2 , (screen_width+50-200,screen_height/2+50))
    
    if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2 <= mouse[1] <= screen_height/2+40: 
        pygame.draw.rect(screen,color_light,[screen_width-200,screen_height/2,140,40])
    
    elif screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2+40 < mouse[1] <= screen_height/2+140:
        pygame.draw.rect(screen,color_light,[screen_width-200,screen_height/2+40,140,40])

    # updates the frames of the game 
    pygame.display.update()
