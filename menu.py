import pygame
import game
from gui import *

pygame.font.init()

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
    font = pygame.font.SysFont(None, 17)
    text = font.render('Welcome to Caves !', False, (0, 0, 0))
    gameDisplay.blit(text, (10, 10))

    display_buttons(gameDisplay, [100, 100, 75, 50], 'Start', green, dim_green)

    # mouse = pygame.mouse.get_pos()
    # text = pygame.font.SysFont(None, 17).render("Click to Start", True, black)
    title = pygame.font.SysFont(None, 50)\
        .render("Snake Thing Game", False, black)
    center_text(gameDisplay, "Snake Thing Game", 500, 100, 50)


while not started:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            started = True
    draw_menu()
    pygame.display.update()
    game.game_mgr.clock.tick(60)


game.start()
