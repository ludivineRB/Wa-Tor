import pygame 
import sys
# import main
  
  
# initializing the constructor 
pygame.init() 
  
# initialize screen
res = (1920,1080) 
screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()
  
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
width = screen.get_width() 
height = screen.get_height() 
  
# creating text for buttons
smallfont = pygame.font.SysFont('Corbel',35) 
text1 = smallfont.render('start' , True , white)
text2 = smallfont.render('quit' , True , white)
title = smallfont.render('Wa-Tor', True, black)
shark_text = smallfont.render('number of shark: ', True, black)
fish_text = smallfont.render('number of fish: ', True, black)


def drawGrid(list_of_sharks, list_of_fish):
    """
        function that draws the world and the animals that live on it

        args
        a list of fish and a list of sharks to draw their position in the world

        returns
        none
    """
    block_size = 50
    grid_width = 20
    grid_height = 20
    for x in range(grid_width):
        for y in range(grid_height):
            rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
            pygame.draw.rect(screen, black, rect,1)
            if (x,y) in list_of_fish:
                pygame.draw.rect(screen, red, rect)
            elif (x,y) in list_of_sharks:
                pygame.draw.rect(screen, grey, rect)

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
            if width-200 <= mouse[0] <= width-60 and height/2 <= mouse[1] <= height/2+40:
                drawGrid([(1,0),(0,1),(0,0),(2,2)],[(3,4),(5,4),(6,6)])
            
            if width-200 <= mouse[0] <= width-60 and height/2+40 < mouse[1] <= height/2+140:
                pygame.quit()
                  
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
    
    #create buttons with text on them and change colour if mouse hovers over them
    pygame.draw.rect(screen,color_dark,[width-200,height/2,140,40]) 
    pygame.draw.rect(screen,color_dark,[width-200,height/2+40,140,40]) 
    screen.blit(text1 , (width+50-200,height/2))
    screen.blit(text2 , (width+50-200,height/2+50))

    #create title
    pygame.draw.rect(screen, blue,[width-200,0,140,40])
    screen.blit(title, (width-200,0))

    #create info text
    pygame.draw.rect(screen, grey,[width-400,40,400,40])
    screen.blit(shark_text, (width-400,40))
    pygame.draw.rect(screen, red,[width-400,80,400,40])
    screen.blit(fish_text, (width-400,80))
    
    if width-200 <= mouse[0] <= width-60 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(screen,color_light,[width-200,height/2,140,40])
    
    elif width-200 <= mouse[0] <= width-60 and height/2+40 < mouse[1] <= height/2+140:
        pygame.draw.rect(screen,color_light,[width-200,height/2+40,140,40])


    # updates the frames of the game 
    pygame.display.update() 
