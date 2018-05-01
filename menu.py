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


def draw_menu():
    gameDisplay.fill(game.white)
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Some Text', False, (0, 0, 0))
    gameDisplay.blit(textsurface, (0, 0))
    # display_buttons(gameDisplay, [100, 100, 10, 10], 'Start', green, dim_green)


while not started:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    draw_menu()
    pygame.display.update()
    game.game_mgr.clock.tick(60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

game.start()
