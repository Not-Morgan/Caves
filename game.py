import pygame

display_height = 1000
display_width = 1000
fps = 60

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('CAVES!')
clock = pygame.time.Clock()
crashed = False


def draw():
    pass


def take_input():
    pass


def logic():
    pass


while not crashed:
    draw()
    take_input()
    logic()
