import pygame
import game
import webbrowser
from gui import *

# define display and caption
gameDisplay = game.game_mgr.gameDisplay
pygame.display.set_caption('Welcome')
info = False
credits = False
started = False

# start intro sound
intro_sound.set_volume(1.0)                                    
intro_sound.play(-1, fade_ms=3000)

# define button positions
start_button_pos = [460, 180, 80, 40]
web_button_pos = [430, 400, 140, 40]
help_button_pos = [455, 300, 90, 40]
credits_button_pos = [450, 500, 100, 40]
back_button_pos = [20, 20, 80, 40]


def draw_menu():

    # draws main menu
    global info
    global credits

    # if started already, don't draw any of the buttons
    if started:
        return True

    gameDisplay.blit(img, (0, 0))
    center_text(gameDisplay, 'Welcome to Caves!', 70, 10, 17, white)

    # mouse = pygame.mouse.get_pos() - dont need this anymore
    # print(int((str(pygame.time.get_ticks())[:-2])[-1:])) testing time thing
    # flashing click to start
    if int((str(pygame.time.get_ticks())[:-2])[-1:]) > 5:
        center_text(gameDisplay, "Click the button below to Start", 500, 150, 25, white)

    center_text(gameDisplay, "Caves!", 500, 100, 50, white)

    if display_buttons(gameDisplay, web_button_pos, 'Visit us on Github', red, dim_red):
        button_click.play(1, 0, 0)
        webbrowser.open("https://github.com/Not-Morgan/Caves")

    if display_buttons(gameDisplay, credits_button_pos, 'Credits', grey, dim_grey) or credits:
        if not credits:
            button_click.play(1, 0, 0)
            pygame.display.set_caption('Credits')
        # button_click.play(1,0,0)

        gameDisplay.fill(white)
        gameDisplay.blit(credits_info, (-17, 0))
        # center_text(gameDisplay, "CREDITS", 500, 20, 50, black)

        credits = True

        if display_buttons(gameDisplay, back_button_pos, '<- Go Back', grey, dim_grey):
            button_click.play(1, 0, 0)
            pygame.display.set_caption('Welcome')
            credits = False

        return False

    if display_buttons(gameDisplay, help_button_pos, 'Need help?', blue, dim_blue) or info:
        if not info:
            button_click.play(1, 0, 0)
            pygame.display.set_caption('Help')
        # button_click.play(1,0,0)
        
        gameDisplay.fill(white)
        gameDisplay.blit(help_info, (-17, 30))

        info = True

        if display_buttons(gameDisplay, back_button_pos, '<- Go Back', blue, dim_blue):
            button_click.play(1, 0, 0)
            pygame.display.set_caption('Welcome')
            info = False

        return False

    if display_buttons(gameDisplay, web_button_pos, 'Visit us on Github', red, dim_red):
        button_click.play(1, 0, 0)
        webbrowser.open("https://github.com/Not-Morgan/Caves")

    return display_buttons(gameDisplay, start_button_pos, 'Start', green, dim_green)


def start(i):
    pygame.display.set_caption('Loading Caves! ...')
    intro_sound.fadeout(5000)
    if pygame.mixer.get_busy():  # and a certain amount of time has passed
        gameDisplay.blit(img, (0, (i * -1)/2))

        # all of the animation once the button is pressed
        animate_button(gameDisplay, start_button_pos, 1, 'Start', green, i)
        animate_button(gameDisplay, help_button_pos, -1, 'Need help?', dim_blue, i)
        animate_button(gameDisplay, web_button_pos, 1, 'Visit us on Github', dim_red, i)
        animate_button(gameDisplay, credits_button_pos, -1, 'Credits', dim_grey, i)
        animate_text(gameDisplay, [500, 100], 60, 3, "Caves!", white, i, 250)
        animate_text(gameDisplay, [70, 10], 17, -0.5, 'Welcome to Caves!', white, i, 250)
        # display instructions here
        # gameDisplay.fill(white) - testing the fill screen, originally stuck in loop, can't update screen

    else:
        gameDisplay.fill(black)
        gameplay_sound.set_volume(1.0)                                    
        gameplay_sound.play(-1, fade_ms=500)
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
    """


   (  )   /\   _                 (     
    \ |  (  \ ( \.(               )                      _____
  \  \ \  `  `   ) \             (  ___                 / _   \
 (_`    \+   . x  ( .\            \/   \____-----------/ (o)   \_
- .-               \+  ;          (  O                           \____
                          )        \_____________  `              \  /
(__                +- .( -'.- <. - _  VVVVVVV VV V\                 \/
(_____            ._._: <_ - <- _  (--  _AAAAAAA__A_/                  |
  .    /./.+-  . .- /  +--  - .     \______________//_              \_______
  (__ ' /x  / x _/ (                                  \___'          \     /
 , x / ( '  . / .  /                                      |           \   /
    /  /  _/ /    +                                      /              \/
   '  (__/                                             /                  \
   
   Mason you better get the game to work otherwise this dragon will breathe on you and you will become ash.

    """

    if draw_menu():
        started = True
        k += 1
        start(k)

    # print(info) --testing the info button
    # print(started, pygame.time.get_ticks()) - debug timeloop in function problem
    pygame.display.update()
    game.game_mgr.clock.tick(30)
