import pygame
import game
import webbrowser
import time
from gui import *

pygame.font.init()
pygame.init()

# define colours of the buttons

dim_red = (200, 0, 0)
dim_green = (0, 200, 0)
dim_blue = (136, 206, 250)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 191, 255)
black = (0, 0, 0)
white = (255, 255, 255)

# define display and caption
gameDisplay = game.game_mgr.gameDisplay
pygame.display.set_caption('Welcome')
started = False

# set sound
intro_sound = pygame.mixer.Sound("sounds/intro.ogg")
gameplay_sound = pygame.mixer.Sound("sounds/gameplay.ogg")
button_click = pygame.mixer.Sound("sounds/button.ogg")
img = pygame.image.load('caves.jpg')
intro_sound.set_volume(1.0)                                    
intro_sound.play (-1,0,0)


def draw_menu():

    #if started already, don't draw any of the buttons
    if started:
        return True

    gameDisplay.blit(img, (0,0))
    font = pygame.font.SysFont(None, 17)
    text = font.render('Welcome to Caves !', False, white)
    gameDisplay.blit(text, (10, 10))

    

    # mouse = pygame.mouse.get_pos()
    center_text(gameDisplay, "Click here to Start", 500, 150, 25, white)
    center_text(gameDisplay, "Caves!", 500, 100, 50, white)

    if (display_buttons(gameDisplay, [450, 400, 100, 40], 'Visit our Website', red, dim_red)):
        webbrowser.open("https://github.com/Not-Morgan/Caves")

    

    return display_buttons(gameDisplay, [460, 180, 80, 40], 'Start', green, dim_green)



def start():
    intro_sound.fadeout(5000)
    if pygame.mixer.get_busy() == True:
        gameDisplay.blit(img, (0,0))
        # display instructions here
        # gameDisplay.fill(white) - testing the fill screen, originally stuck in loop, can't update screen


    else:
        gameplay_sound.set_volume(1.0)                                    
        gameplay_sound.play (-1,0,0)
        pygame.display.set_caption('CAVES!')
        # print("Game starts") - debug can't start game for some reason
        game.start()
        pygame.quit()
        quit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    """
        if event.type == pygame.KEYDOWN: # Press Spacebar to Start
            if event.key == pygame.K_SPACE:
                start()
    """

    if draw_menu():
        started = True
        start()


    # print(started, pygame.time.get_ticks()) - debug timeloop in function problem
    pygame.display.update()
    game.game_mgr.clock.tick(60)
