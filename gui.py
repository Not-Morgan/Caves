# all the definitions for stuff
import pygame

# define colours of the buttons
black = (0, 0, 0)



pygame.font.init()


def center_text(screen, text, x, y, font_size, colour):
    font = pygame.font.SysFont(None, font_size)
    text = font.render(str(text), True, colour)
    screen.blit(text, (x - text.get_rect().width / 2, y))


def display_buttons(screen, button_pos, text, colour, dim_colour):  # button_pos takes x, y, len x, len y

    mouse = pygame.mouse.get_pos()

    def buttonClicked():
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True

    if button_pos[0] + button_pos[2] > mouse[0] > button_pos[0] and button_pos[1] + button_pos[3] > mouse[1] > button_pos[1]:  # if mouse is inside the button
        pygame.draw.rect(screen, colour, (button_pos[0], button_pos[1], button_pos[2], button_pos[3]))  # change colour
        center_text(screen, text, button_pos[0] + button_pos[2]/2, button_pos[1] + 17, 17, black)
        print(mouse, "in button")
        if buttonClicked():
            print("I am clicked!")
            return str(text)
    else:
        pygame.draw.rect(screen, dim_colour, (button_pos[0], button_pos[1], button_pos[2], button_pos[3]))
        center_text(screen, text, button_pos[0] + button_pos[2]/2, button_pos[1] + 17, 17, black)
        print(mouse, "not in button")

"""
def button_pressed(score, price1, price2, price3, price4):
        
        button1_pos = [515, 100, 75, 50]
        

        mouse = pygame.mouse.get_pos()

        #define the function of if a mouse is clicked in the boundary of the buttons
        
        def buttonClicked(button_pos):
                if button_pos[0] + button_pos[2] > mouse[0] > button_pos[0] and button_pos[1] + button_pos[3] > mouse[1] > button_pos[1]: #if the mouse is in the boundaries of the button
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN: #and the mouse is clicked
                            return True
                

        #checks if the buttons are clicked and returns them to the main script

        if buttonClicked(button1_pos) and score >= price1:
                return "Apple"
        if buttonClicked(button2_pos) and score >= price2:
                return "Snake"
        if buttonClicked(button3_pos) and score >= price3:
                return "Snake2"
        if buttonClicked(button4_pos) and score >= price4:
                return "Snake3"
        if buttonClicked(buttoncheat_pos):
                return "Snake4"
        if buttonClicked(buttoncredits_pos):
                webbrowser.open("https://github.com/Not-Morgan/Caves")
        
        else:
                return "None"
    """
