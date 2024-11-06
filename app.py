import Grid
from Fish import Fish
from class_shark import Shark
import random
import os
import time
import pygame 
import sys
import data
  
# initializing the constructor 
pygame.init() 
  
# initialize screen
res = (1920,1080) 
screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()

# FPS (frames per second) controller
fps = pygame.time.Clock()
pygame.mixer.music.load('Sous locéan (De La Petite SirèneFrench Audio Only).mp3')
pygame.mixer.music.play()
pygame.mixer.music.play(loops = -1)
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
text3 = smallfont.render('graph' , True , white)
text4 = smallfont.render('return' , True , white)
title = bigfont.render('Wa-Tor', True, white)
screen.blit(title, (screen_width/2-150,screen_height/2))
LEFT = 1

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
    list_of_sharks.append(Shark(width,height,shark[0],shark[1],0, 2,0,0,0))


for fish in list_of_random_coordinates[number_of_sharks:]:
    list_of_fish.append(Fish(width,height,fish[0],fish[1],0,0,0,0))

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
            rect = pygame.Rect(x*block_size+150, y*block_size+5, block_size, block_size)
            pygame.draw.rect(screen, blue_grid, rect,1)
            if (x,y) in list_positions_fish:
                nemo = pygame.transform.scale(nemo,(25,25))
                screen.blit(nemo,(x*block_size+150,y*block_size+5))

            elif (x,y) in list_positions_shark:
                shark = pygame.transform.scale(shark,(25,25))
                screen.blit(shark,(x*block_size+150,y*block_size+5))
            
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
    text = 'Number of shark: ' + str(len(list_positions_shark))
    return text

def create_fish_text(list_positions_fish:list[tuple[int,int]])->str:
    """_summary_ return in a string type the number of fish

    Args:
        list_positions_fish (list[tuple[int,int]]): _description_ list of tuples with each position of fish object

    Returns:
        str: _description_ number of fish
    """
    text = 'Number of fish: ' + str(len(list_positions_fish))
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
    data.create_csv(chronon, number_of_fish, number_of_sharks, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    while len(list_of_fish) != 0  and len(list_of_sharks)!=-0:
        drawGrid(list_positions_fish, list_positions_shark)
        nb_shark_text = create_shark_text(list_positions_shark)
        shark_text = smallfont.render(nb_shark_text, True, white)
        nb_fish_text = create_fish_text(list_positions_fish)
        fish_text = smallfont.render(nb_fish_text, True, white)
        chronon_text = create_chronon_text(chronon)
        chronon_metre_text = smallfont.render(chronon_text, True, white)

        screen.blit(shark_text, (screen_width-300,screen_height-900))
        screen.blit(fish_text, (screen_width-300,screen_height-860))
        screen.blit(chronon_metre_text, (screen_width-300,screen_height -820))

        temp_list_positions_fish = []
        temp_list_positions_shark = []
        temp_list_of_fish = []
        temp_list_of_shark = []
        temp_positions_babyshark = []
        temp_positions_babyfish = []
        list_of_shared_positions= [] 
        average_age_fish = 0
        average_age_shark = 0
        average_nb_descendants_fish = 0
        average_nb_descendants_shark = 0
        average_distance_fish = 0
        average_distance_shark = 0

        #loop to move sharks
        for j in range(len(list_of_sharks)):
            x_old = list_of_sharks[j].x_coordinate
            y_old = list_of_sharks[j].y_coordinate
            list_of_sharks[j].move(list_positions_fish, list_positions_shark, temp_positions_babyshark)
            list_of_sharks[j].age += 1
            #checks starvation time of shark
            if list_of_sharks[j].starvation_time == 0:
                pass
            else:
                temp_list_positions_shark.append((list_of_sharks[j].x_coordinate, list_of_sharks[j].y_coordinate))
                temp_list_of_shark.append(list_of_sharks[j])
                list_positions_shark[j] =(list_of_sharks[j].x_coordinate, list_of_sharks[j].y_coordinate)
                if list_of_sharks[j].x_coordinate != x_old or list_of_sharks[j].y_coordinate != y_old:
                    list_of_sharks[j].distance += 1
                #reproduction of sharks
                if list_of_sharks[j].reproduction_time > 6:
                    if list_of_sharks[j].x_coordinate != x_old or list_of_sharks[j].y_coordinate != y_old:
                        temp_list_of_shark.append(Shark(height, width, x_old,y_old, 0,2,0,0,0))
                        temp_list_positions_shark.append((x_old, y_old))
                        list_of_sharks[j].reproduction_time = 0
                        temp_positions_babyshark.append((x_old,y_old))
                        list_of_sharks[j].nb_descendants += 1


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
                if list_of_fish[i].x_coordinate != x_old or list_of_fish[i].y_coordinate != y_old:
                    list_of_fish[i].distance += 1
                #reproduction of fish
                if list_of_fish[i].reproduction_time > 1:
                    if list_of_fish[i].x_coordinate != x_old or list_of_fish[i].y_coordinate != y_old:
                        list_of_fish[i].distance += 1
                        temp_list_of_fish.append(Fish(height, width, x_old,y_old, 0,0,0,0))
                        temp_list_positions_fish.append((x_old, y_old))
                        list_of_fish[i].reproduction_time = 0
                        temp_positions_babyfish.append((x_old,y_old))
                        list_of_fish[i].nb_descendants += 1

        #update list
        list_positions_shark = temp_list_positions_shark
        list_of_sharks = temp_list_of_shark
        list_of_fish = temp_list_of_fish   
        list_positions_fish = temp_list_positions_fish
        chronon += 1
        max_nb_descendants_fish = 0
        max_nb_descendants_shark = 0
        max_distance_fish = 0
        max_distance_shark = 0

        for fish in list_of_fish:
            average_age_fish+=fish.age
            average_nb_descendants_fish += fish.nb_descendants
            average_distance_fish += fish.distance
        if fish.nb_descendants > max_nb_descendants_fish:
            max_nb_descendants_fish = fish.nb_descendants
        if fish.distance > max_distance_fish:
            max_distance_fish = fish.distance



        average_age_fish = int(average_age_fish/len(list_of_fish))
        average_nb_descendants_fish = int(average_nb_descendants_fish/len(list_of_fish))
        average_distance_fish = int(average_distance_fish/len(list_of_fish))

        for shark in list_of_sharks:
            average_age_shark+=shark.age
            average_nb_descendants_shark += shark.nb_descendants
            average_distance_shark += shark.distance
            if shark.nb_descendants > max_nb_descendants_shark:
                max_nb_descendants_shark = shark.nb_descendants
            if shark.distance > max_distance_shark:
                max_distance_shark = shark.distance


        average_age_shark = int(average_age_shark/len(list_of_sharks))
        average_nb_descendants_shark = int(average_nb_descendants_shark/len(list_of_sharks))
        average_distance_shark = int(average_distance_shark/len(list_of_sharks))

        data.update_csv(chronon, len(list_of_fish),len(list_of_sharks),average_age_fish, average_age_shark,average_nb_descendants_fish, 
               average_nb_descendants_shark, average_distance_fish, average_distance_shark, 
               max_nb_descendants_fish, max_nb_descendants_shark, max_distance_fish, max_distance_shark)
        data.create_plot()
        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT: 
                pygame.quit()  
            #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == LEFT: 
                if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2+40 < mouse[1] <= screen_height/2+80:
                    pygame.quit()
                if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2< mouse[1] <= screen_height/2+40:
                    open_graph()
                
                
                
        # stores the (x,y) coordinates into the variable as a tuple 
        mouse = pygame.mouse.get_pos() 
        
        pygame.draw.rect(screen,color_dark,[screen_width-200,screen_height/2+40,140,40]) 
        screen.blit(text2 , (screen_width+50-200,screen_height/2+45))
        pygame.draw.rect(screen,color_dark,[screen_width-200,screen_height/2,140,40]) 
        screen.blit(text3 , (screen_width+50-200,screen_height/2+5))

        if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2+40 <= mouse[1] <= screen_height/2+80: 
            pygame.draw.rect(screen,color_light,[screen_width-200,screen_height/2+40,140,40])
            screen.blit(text2 , (screen_width+50-200,screen_height/2+45))
        elif  screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2 < mouse[1] <= screen_height/2+40:
            pygame.draw.rect(screen,color_light,[screen_width-200,screen_height/2,140,40])
            screen.blit(text3 , (screen_width+50-200,screen_height/2+5))

        #events as in button clicks
        pygame.display.update()
        fps.tick(10)

def open_graph():
    screen = pygame.display.set_mode(res)
    continuer = True
    while continuer:
        ocean_waves = pygame.image.load("ocean-waves.jpg") 
        ocean_waves = pygame.transform.scale(ocean_waves,res)
        #display of the 'ocean_waves' paper wall
        screen.blit(ocean_waves, (0,0)) 
        graph= pygame.image.load("data.png")
        graph2=pygame.image.load("distance.png")
        #display of the graph
        screen.blit(graph, (screen_width/2-850,screen_height/2-300)) 
        screen.blit(graph2, (screen_width/2-10,screen_height/2-300)) 
        pygame.draw.rect(screen,color_dark,[screen_width-200,screen_height/2,140,40])
        screen.blit(text4 , (screen_width+50-200,screen_height/2+5))
        pygame.draw.rect(screen,color_dark,[screen_width-200,screen_height/2+40,140,40])
        screen.blit(text2 , (screen_width+50-200,screen_height/2+45))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT: 
                if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2 < mouse[1] <= screen_height/2+40:
                    continuer=False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT: 
                if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2+40 < mouse[1] <= screen_height/2+80:
                    pygame.quit()

        mouse = pygame.mouse.get_pos()    
        if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2 <= mouse[1] <= screen_height/2+40: 
            pygame.draw.rect(screen,color_light,[screen_width-200,screen_height/2,140,40])
            screen.blit(text4 ,(screen_width+50-200,screen_height/2+5))
        elif screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2+40<= mouse[1] <= screen_height/2+80: 
            pygame.draw.rect(screen,color_light,[screen_width-200,screen_height/2+40,140,40])
            screen.blit(text2 ,(screen_width+50-200,screen_height/2+45))


        #pygame.display.update()      
        pygame.display.flip()

    pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Simulator")
#infinite loop to run pygame
while True:
    #events as in button clicks
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == LEFT: 
              
            #if the mouse is clicked on the button the game is terminated 
            if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2 <= mouse[1] <= screen_height/2+40:
                main_pygame(list_positions_fish,list_positions_shark,list_of_fish, list_of_sharks)
                #drawGrid(list_positions_fish,list_positions_shark)

            if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2+40 < mouse[1] <= screen_height/2+80:
                pygame.quit()
    # while mouse_pressed:
    # stores the (x,y) coordinates into the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
    
    #create buttons with text on them and change colour if mouse hovers over them
    pygame.draw.rect(screen,color_dark,[screen_width-200,screen_height/2,140,40]) 
    pygame.draw.rect(screen,color_dark,[screen_width-200,screen_height/2+40,140,40]) 
    
    screen.blit(text1 , (screen_width+50-200,screen_height/2+5))
    screen.blit(text2 , (screen_width+50-200,screen_height/2+45))
    
    if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2 <= mouse[1] <= screen_height/2+40: 
        pygame.draw.rect(screen,color_light,[screen_width-200,screen_height/2,140,40])
        screen.blit(text1 , (screen_width+50-200,screen_height/2+5))
    elif screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2+40 < mouse[1] <= screen_height/2+80:
        pygame.draw.rect(screen,color_light,[screen_width-200,screen_height/2+40,140,40])
        screen.blit(text2 , (screen_width+50-200,screen_height/2+45))
    # updates the frames of the game 
    pygame.display.update()
