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

#initalize dimensions
screen_width = screen.get_width() 
screen_height = screen.get_height() 
  
# creating text for buttons
smallfont = pygame.font.SysFont('Corbel',35) 
text1 = smallfont.render('start' , True , white)
text2 = smallfont.render('quit' , True , white)
title = smallfont.render('Wa-Tor', True, black)

height = 10
width = 10

#initialize number of animals
number_of_sharks = 2
number_of_fish = 5
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

def drawGrid(list_positions_fish, list_positions_shark):
    """
        function that draws the world and the animals that live on it

        args
        a list of fish and a list of sharks to draw their position in the world

        returns
        none
    """
    block_size = 50
    grid_width = width
    grid_height = height
    for x in range(grid_width):
        for y in range(grid_height):
            rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
            pygame.draw.rect(screen, black, rect,1)
            if (x,y) in list_positions_fish:
                pygame.draw.rect(screen, red, rect)

            elif (x,y) in list_positions_shark:
                pygame.draw.rect(screen, grey, rect)
            
            else:
                pygame.draw.rect(screen, blue, rect)
                
            pygame.draw.rect(screen, black, rect,1)

def create_shark_text(list_positions_shark):
    text = 'number of shark: ' + str(len(list_positions_shark))
    return text

def create_fish_text(list_positions_fish):
    text = 'number of fish: ' + str(len(list_positions_fish))
    return text

def main_pygame(list_positions_fish,list_positions_shark):
    drawGrid(list_positions_fish,list_positions_shark)
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
    return list_positions_fish, list_positions_shark

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
                #infinite loop that will print to console 1 for fish 2 for shark and 0 for nothing
                while len(list_of_fish) != 0 and len(list_of_sharks) != 0:
                    #create info text
                    nb_shark_text = create_shark_text(list_positions_shark)
                    shark_text = smallfont.render(nb_shark_text, True, black)
                    nb_fish_text = create_fish_text(list_positions_fish)
                    fish_text = smallfont.render(nb_fish_text, True, black)
                    pygame.draw.rect(screen, grey,[screen_width-400,40,400,40])
                    screen.blit(shark_text, (screen_width-400,40))
                    pygame.draw.rect(screen, red,[screen_width-400,80,400,40])
                    screen.blit(fish_text, (screen_width-400,80))

                    pygame.display.update()
                    fps.tick(1)

                    (list_positions_fish, list_positions_shark) = main_pygame(list_positions_fish,list_positions_shark)


            if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2+40 < mouse[1] <= screen_height/2+140:
                pygame.quit()
                  
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
    
    #create buttons with text on them and change colour if mouse hovers over them
    pygame.draw.rect(screen,color_dark,[screen_width-200,screen_height/2,140,40]) 
    pygame.draw.rect(screen,color_dark,[screen_width-200,screen_height/2+40,140,40]) 
    screen.blit(text1 , (screen_width+50-200,screen_height/2))
    screen.blit(text2 , (screen_width+50-200,screen_height/2+50))

    #create title
    pygame.draw.rect(screen, blue,[screen_width-200,0,140,40])
    screen.blit(title, (screen_width-200,0))

    
    if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2 <= mouse[1] <= screen_height/2+40: 
        pygame.draw.rect(screen,color_light,[screen_width-200,screen_height/2,140,40])
    
    elif screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2+40 < mouse[1] <= screen_height/2+140:
        pygame.draw.rect(screen,color_light,[screen_width-200,screen_height/2+40,140,40])


    # updates the frames of the game 
    pygame.display.update()
