import pygame
import game
from gui import *

# define colours of the buttons
dim_red = (200, 0, 0)
dim_green = (0, 200, 0)
dim_blue = (136, 206, 250)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 191, 255)
black = (0, 0, 0)

gameDisplay = game.game_mgr.gameDisplay
pygame.display.set_caption('Welcome')
started = False


def drawmenu():
    display_buttons(gameDisplay, [100, 100, 10, 10], 'Start', green, dim_green)


while not started:
    drawmenu()
    pygame.display.update()
    game.game_mgr.clock.tick(60)

game.start()
