import pygame 
import functionalities
import list_creation
  
#initialize the constructor 
pygame.init() 
  
#initialize screen
res = (1920,1080) 
screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()

#FPS (frames per second) controller
fps = pygame.time.Clock()

#initialize music
pygame.mixer.music.load('media/Sous locéan (De La Petite SirèneFrench Audio Only).mp3')
pygame.mixer.music.play(loops = -1)

#initialize colours
white = (255,255,255) 
color_light = (170,170,170) 
color_dark = (100,100,100)   
blue_grid = (204,229,255)

#initialize dimensions
screen_width = screen.get_width() 
screen_height = screen.get_height()
ocean_waves = pygame.image.load("media/ocean-waves.jpg") 
ocean_waves = pygame.transform.scale(ocean_waves,res)
screen.blit(ocean_waves, (0,0))
  
#initialize text 
smallfont = pygame.font.SysFont('Corbel',35)
bigfont = pygame.font.SysFont('Corbel',200)
text1 = smallfont.render('start' , True , white)
text2 = smallfont.render('quit' , True , white)
text3 = smallfont.render('graph' , True , white)
text4 = smallfont.render('return' , True , white)
title = bigfont.render('Wa-Tor', True, white)
screen.blit(title, (screen_width/2-150,screen_height/2))
LEFT = 1

#initialize Grid dimensions
height = 40
width = 40

#initialize number of animals
number_of_sharks = 25
number_of_fish = 200
number_of_animals = number_of_sharks + number_of_fish
list_of_fish, list_of_sharks, list_positions_fish, list_positions_shark = list_creation.list_creation(height, width, number_of_sharks, number_of_animals)

#Start the graphic display and the simulation
while True:
    #events as in button clicks
    for ev in pygame.event.get(): 
        if ev.type == pygame.QUIT: 
            pygame.quit()     
        #check if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == LEFT: 
            #start the simulation
            if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2 <= mouse[1] <= screen_height/2+40:
                functionalities.main_pygame(list_positions_fish,list_positions_shark,list_of_fish, list_of_sharks, number_of_sharks, number_of_fish, screen_width, screen_height, screen, width, height, blue_grid, res, text2, text3, text4, white, LEFT,
                color_light, color_dark, fps)
            #quit the simulation
            if screen_width-200 <= mouse[0] <= screen_width-60 and screen_height/2+40 < mouse[1] <= screen_height/2+80:
                pygame.quit()

    #store the (x,y) coordinates into the variable as a tuple 
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
