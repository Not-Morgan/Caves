# all the definitions for stuff
import pygame

# define colours of the buttons
black = (0, 0, 0)



pygame.font.init()


def center_text(screen, text, x, y, font_size):
    font = pygame.font.SysFont(None, font_size)
    text = font.render(str(text), True, black)
    screen.blit(text, (x - text.get_rect().width / 2, y))


def display_buttons(screen, button_pos, text, colour, dim_colour):  # button_pos takes x, y, len x, len y
    mouse = pygame.mouse.get_pos()
    if button_pos[0] + button_pos[2] > mouse[0] > button_pos[0] and button_pos[1] + button_pos[3] > mouse[1] > button_pos[1]:  # if mouse is inside the button
        pygame.draw.rect(screen, colour, (button_pos[0], button_pos[1], button_pos[2], button_pos[3]))  # change colour
        center_text(screen, text, button_pos[0] + button_pos[2]/2, button_pos[1] + 17, 17)
        print(mouse, "in button")
        # for event in pygame
        # if pygame.mouse.get_pressed()[]
        return text
    else:
        pygame.draw.rect(screen, dim_colour, (button_pos[0], button_pos[1], button_pos[2], button_pos[3]))
        center_text(screen, text, button_pos[0] + button_pos[2]/2, button_pos[1] + 17, 17)
        print(mouse, "not in button")
