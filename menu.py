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

    if (display_buttons(gameDisplay, [460, 180, 80, 40], 'Start', green, dim_green)) == 'Start':
        started = False

    # mouse = pygame.mouse.get_pos()
    center_text(gameDisplay, "Click here to Start", 500, 150, 25)

    center_text(gameDisplay, "Caves!", 500, 100, 50)


while not started:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.start()
                pygame.quit()
    draw_menu()
    pygame.display.update()
    game.game_mgr.clock.tick(60)
    print(started)


game.start()
