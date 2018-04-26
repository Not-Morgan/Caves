import pygame
import mobs
import world

display_height = 1000
display_width = 1000
fps = 60

player_rot = 0
player_mov = 0

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('CAVES!')
clock = pygame.time.Clock()
crashed = False


def draw():
    gameDisplay.fill(black)

    for c in world.caves:
        pygame.draw.circle(gameDisplay, white, list(map(int, c.pos)), c.radius, 0)

    pygame.draw.circle(gameDisplay, blue, list(map(int, player.pos)), 7, 0)

    pygame.display.update()
    clock.tick(fps)


def take_input():
    global crashed
    global player_mov
    global player_rot

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # x button is pressed
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                print(player.pos, player.direction)

            # player movement
            if event.key == pygame.K_w:
                player_mov += 1
            if event.key == pygame.K_s:
                player_mov -= 1
            if event.key == pygame.K_a:
                player_rot -= 5
            if event.key == pygame.K_d:
                player_rot += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_mov -= 1
            if event.key == pygame.K_s:
                player_mov += 1
            if event.key == pygame.K_a:
                player_rot += 5
            if event.key == pygame.K_d:
                player_rot -= 5


def logic():
    # player movement
    if player_mov == 1:
        player.move()
    if player_mov == -1:
        player.move(-0.5)
    player.rotate(player_rot)


# TODO main menu

player = mobs.Player([500, 500])
world = world.WorldManager()

while not crashed:
    draw()
    take_input()
    logic()
