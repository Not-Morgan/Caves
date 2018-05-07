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

start_button_pos = [460, 180, 80, 40]
web_button_pos = [450, 400, 100, 40]


def draw_menu():
    

    # if started already, don't draw any of the buttons
    if started:
        return True

    gameDisplay.blit(img, (0,0))
    font = pygame.font.SysFont(None, 17)
    text = font.render('Welcome to Caves !', False, white)
    gameDisplay.blit(text, (10, 10))

    

    # mouse = pygame.mouse.get_pos() - dont need this anymore
    # print(int((str(pygame.time.get_ticks())[:-2])[-1:])) testing time thing
    # flashing click to start
    if int((str(pygame.time.get_ticks())[:-2])[-1:]) > 5:
        center_text(gameDisplay, "Click the button below to Start", 500, 150, 25, white)

    center_text(gameDisplay, "Caves!", 500, 100, 50, white)

    if display_buttons(gameDisplay, web_button_pos, 'Visit us on Github', red, dim_red):
        webbrowser.open("https://github.com/Not-Morgan/Caves")

    

    return display_buttons(gameDisplay, start_button_pos, 'Start', green, dim_green)




def animate_button(pos, speed, text, colour, count):
    # print(count) - testing the animate before implementation
    pos[0] = pos[0] + (count * speed)
    display_buttons(gameDisplay, pos, text, colour, colour)


def animate_text(pos, font_size, speed, text, colour, count):
    pos[1] = pos[1] + (count * speed)
    center_text(gameDisplay, text, pos[0], pos[1], font_size, colour)




def start(i):
    intro_sound.fadeout(6000)
    if pygame.mixer.get_busy() == True:
        gameDisplay.blit(img, (0,0))

        # all of the animation once the button is pressed
        animate_button(start_button_pos , 1, 'Start', green, i)
        animate_button(web_button_pos, -1, 'Visit us on Github', red, i)
        animate_text([500, 100], 50, 1.5, "Caves!", white, i)
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


k = 0
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
        k += 1
        start(k)


    # print(started, pygame.time.get_ticks()) - debug timeloop in function problem
    pygame.display.update()
    game.game_mgr.clock.tick(60)
