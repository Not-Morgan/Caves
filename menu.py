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
white = (255, 255, 255)

gameDisplay = game.game_mgr.gameDisplay
pygame.display.set_caption('Welcome')
started = False

def initialization():
    pygame.init()
    # set sound
    intro_sound = pygame.mixer.Sound("sounds/intro.ogg")
    gameplay_sound = pygame.mixer.Sound("sounds/gameplay.ogg")
    button_click = pygame.mixer.Sound("sounds/button.ogg")
    img = pygame.image.load('caves.jpg')
    gameDisplay.blit(img, (0,0))
    intro_sound.set_volume(1.0)                                    
    intro_sound.play (-1,0,0)


def draw_menu():
    gameDisplay.fill(game.white)
    img = pygame.image.load('caves.jpg')
    gameDisplay.blit(img, (0,0))
    font = pygame.font.SysFont(None, 17)
    text = font.render('Welcome to Caves !', False, white)
    gameDisplay.blit(text, (10, 10))

    if (display_buttons(gameDisplay, [460, 180, 80, 40], 'Start', green, dim_green)) == 'Start':
        started = True

    # mouse = pygame.mouse.get_pos()
    center_text(gameDisplay, "Click here to Start", 500, 150, 25, white)
    center_text(gameDisplay, "Caves!", 500, 100, 50, white)



initialization()
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
