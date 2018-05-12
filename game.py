import pygame
import world
import mobs
import gui
from random import randint

display_height = 700
display_width = 1000
fps = 45

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()
game_over = pygame.mixer.Sound("static/sounds/deathmusic.ogg")
game_over.set_volume(1.0)


class GameManager:
    player_rot = 0
    player_mov = 0
    screen_x = 0
    screen_y = 0
    crashed = False

    def __init__(self):
        pygame.init()
        self.gameDisplay = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('CAVES!')
        self.clock = pygame.time.Clock()

    def draw(self):
        self.gameDisplay.fill(black)

        world_mgr.render(self.gameDisplay)

        # draw player
        pygame.draw.circle(self.gameDisplay, blue,
                           [int(player.pos[0] + self.screen_x), int(player.pos[1] + self.screen_y)], 7, 0)

        mob_mgr.render(self.gameDisplay)

        pygame.display.update()
        self.clock.tick(fps)

    def take_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # x button is pressed
                self.crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    mob_mgr.new_mob(world.Chest, [pygame.mouse.get_pos()[0] - self.screen_x,
                                                  pygame.mouse.get_pos()[1] - self.screen_y], {"bombs": 5})
                    print(player.bombs)
                if event.key == pygame.K_c:
                    mob_mgr.new_mob(mobs.Enemy, [pygame.mouse.get_pos()[0] - self.screen_x,
                                                 pygame.mouse.get_pos()[1] - self.screen_y])
                if event.key == pygame.K_m:
                    world_mgr.make_cave(
                        [pygame.mouse.get_pos()[0] - self.screen_x, pygame.mouse.get_pos()[1] - self.screen_y], 25, 40)

                if event.key == pygame.K_SPACE:
                    player.shoot()
                if event.key == pygame.K_e:
                    player.throw_bomb()

                # moving
                if event.key == pygame.K_w:
                    self.player_mov += 1
                if event.key == pygame.K_s:
                    self.player_mov -= 1
                if event.key == pygame.K_a:
                    self.player_rot -= 5
                if event.key == pygame.K_d:
                    self.player_rot += 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.player_mov -= 1
                if event.key == pygame.K_s:
                    self.player_mov += 1
                if event.key == pygame.K_a:
                    self.player_rot += 5
                if event.key == pygame.K_d:
                    self.player_rot -= 5

    def logic(self):
        # player movement
        if self.player_mov == 1:
            player.move()
        if self.player_mov == -1:
            player.move(-0.5)
        player.rotate(self.player_rot * 2)

        if player.health < 1:
            self.player_death()
            self.crashed = True

        if not randint(0, 120):
            world_mgr.extend_caves(player.pos)

        mob_mgr.move_all()

        self.screen_x = 500 - player.pos[0]
        self.screen_y = 500 - player.pos[1]

    def mainloop(self):
        while not self.crashed:
            self.draw()
            self.take_input()
            self.logic()

    def player_death(self):
        self.gameDisplay.fill(black)
        game_over.play(-1, 0, 0)
        gui.center_text(self.gameDisplay, "You have died! I am disappointed in you", 400, 300, 60, white)

    def sidebar(self):
        pygame.draw.rect(self.gameDisplay, white, (800, 0, 200, 200), width=5)
        gui.center_text(self.gameDisplay, "Thou hath" + player.bombs + "bombs", 900, 10, 12, white)


game_mgr = GameManager()
world_mgr = None
player = None
mob_mgr = None


def start():
    global world_mgr
    global player
    global mob_mgr
    world_mgr = world.WorldManager()
    player = mobs.Player([500, 500])
    mob_mgr = mobs.MobManager()
    world_mgr.generate_world()

    game_mgr.mainloop()
