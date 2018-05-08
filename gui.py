# all the definitions for stuff

import pygame

# define colours of the buttons
black = (0, 0, 0)

button_click = pygame.mixer.Sound("sounds/button.ogg")

pygame.font.init()


def center_text(screen, text, x, y, font_size, colour):
    font = pygame.font.SysFont(None, font_size)
    text = font.render(str(text), True, colour)
    screen.blit(text, (x - text.get_rect().width / 2, y))


def button_clicked():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            return True
        else:
            return False


def display_buttons(screen, button_pos, text, colour, dim_colour):  # button_pos takes x, y, len x, len y

    mouse = pygame.mouse.get_pos()

    if button_pos[0] + button_pos[2] > mouse[0] > button_pos[0] and \
            button_pos[1] + button_pos[3] > mouse[1] > button_pos[1]:  # if mouse is inside the button
        pygame.draw.rect(screen, colour, (button_pos[0], button_pos[1], button_pos[2], button_pos[3]))  # change colour
        center_text(screen, text, button_pos[0] + button_pos[2]/2, button_pos[1] + 17, 17, black)
        # print(mouse, "in button")
        if button_clicked():
            return True
    else:
        pygame.draw.rect(screen, dim_colour, (button_pos[0], button_pos[1], button_pos[2], button_pos[3]))
        center_text(screen, text, button_pos[0] + button_pos[2]/2, button_pos[1] + 17, 17, black)
        # print(mouse, "not in button")
        return False
# animation goes here after debugging to clean up the files


def animate_button(display, pos, speed, text, colour, count):
    # print(count) - testing the animate before implementation
    pos[0] = pos[0] + (count * speed)
    display_buttons(display, pos, text, colour, colour)


def animate_text(display, pos, font_size, speed, text, colour, count, end_limit):
    if pos[1] + (count * speed) < end_limit:
        pos[1] = pos[1] + (count * speed)
    else:
        while not(pos[1] + (count * speed) < end_limit):
            count -= 1

        pos[1] = pos[1] + (count * speed)
    center_text(display, text, pos[0], pos[1], font_size, colour)


"""
___________((_____))
____________))___((
___________((_____))
____________))___((
___________((_____))____________$$$$$$
____________))___((____________$$____$$
_$$$$$$$$$$$$$$$$$$$$$$$$$$$$$______$$
__$$$$$$$$$$$$$$$$$$$$$$$$$$$_______$$
___$$$$$$$$$$$$$$$$$$$$$$$$________$$
____$$$$$$$$$$$$$$$$$$$$$$________$$
____$$$$$$$$$$$$$$$$$$$$$$______$$
_____$$$$$$$$$$$$$$$$$$$$_____$$
_____$$$$$$$$$$$$$$$$$$$$$$$$$
______$$$$$$$$$$$$$$$$$$
_______$$$$$$$$$$$$$$$$
_________$$$$$$$$$$$$
___________$$$$$$$$
_$$$$$$$$$$$$$$$$$$$$$$$$$$$$
___$$$$$$$$$$$$$$$$$$$$$$$$
_____$$$$$$$$$$$$$$$$$$$$__

Coffee?

"""
