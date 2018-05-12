import pygame
import extra_math as math
import game
from random import randint


class Mob:
    health = 5
    direction = 0
    speed = 1
    size = 7

    def __init__(self, pos):
        self.pos = pos
        self.colour = game.blue

    def move(self, dist=None):
        if dist is None:
            dist = self.speed

        # move based on direction
        self.pos[0] += math.cos(math.radians(self.direction)) * dist
        self.pos[1] += math.sin(math.radians(self.direction)) * dist

        # undo if you went into a wall
        if not math.in_circles(self.pos, game.world_mgr.caves):
            self.pos[0] -= math.cos(math.radians(self.direction)) * dist
            self.pos[1] -= math.sin(math.radians(self.direction)) * dist
            return True
        return False

    def rotate(self, degrees):
        self.direction = (self.direction + degrees) % 360

    def change_health(self, amount):
        self.health += amount


class Enemy(Mob):
    health = 3
    speed = 0.75

    def exist(self):
        # if the player is close more towards the player
        if math.hypo(self.pos, game.player.pos) < 50:
            self.direction = math.angle_between(self.pos, game.player.pos)
            # if the player is close deal damage and move back
            if math.hypo(self.pos, game.player.pos) < 15:
                game.player.change_health(-1)
                if self.move(self.speed * -1):
                    self.rotate(180)
        else:
            self.rotate(randint(-10, 10))
        if self.move():
            self.rotate(180)
        if self.health < 1:
            game.player.add_points(5)
            return False
        return True


# 2D - Applying Abstraction
class Player(Mob):
    points = 0
    bombs = 10
    speed = 1.5
    health = 100

    def __init__(self, pos):
        super().__init__(pos)

    def move(self, dist=None):
        if dist is None:
            dist = self.speed

        # move based on direction
        self.pos[0] += math.cos(math.radians(self.direction)) * dist
        self.pos[1] += math.sin(math.radians(self.direction)) * dist

        # game.game_mgr.screen_x += math.cos(math.radians(self.direction)) * dist
        # game.game_mgr.screen_y += math.sin(math.radians(self.direction)) * dist

        # undo if you went into a wall
        if not math.in_circles(self.pos, game.world_mgr.caves):
            self.pos[0] -= math.cos(math.radians(self.direction)) * dist
            self.pos[1] -= math.sin(math.radians(self.direction)) * dist

            # game.game_mgr.screen_x -= math.cos(math.radians(self.direction)) * dist
            # game.game_mgr.screen_y -= math.sin(math.radians(self.direction)) * dist
            return True
        return False

    def shoot(self):
        for i in range(5):
            game.mob_mgr.new_mob(Bullet, [self.pos[0], self.pos[1]], self.direction + randint(-10, 10))

    def throw_bomb(self):
        game.mob_mgr.new_mob(Bomb, [self.pos[0], self.pos[1]], self.direction)
        self.bombs -= 1

    def add_bombs(self, amount):
        self.bombs += amount

    def add_points(self, amount):
        self.points += amount


class Bomb(Mob):
    wait_time = 1000
    radius = 25
    speed = 2
    size = 4

    def __init__(self, pos, direction):
        super().__init__(pos)
        self.direction = direction
        self.create_time = pygame.time.get_ticks()

    def exist(self):
        # explode otherwise move
        if pygame.time.get_ticks() - self.create_time > self.wait_time:
            self.explode()
            return False
        else:
            super().move(self.speed)
            return True

    def explode(self):
        game.world_mgr.add_hole(self.pos, self.radius)


class Bullet(Mob):
    wait_time = 1000
    speed = 5
    size = 2

    def __init__(self, pos, direction):
        super().__init__(pos)
        self.direction = direction
        self.create_time = pygame.time.get_ticks()

    def exist(self):
        # if it has existed for some time it disappears
        if pygame.time.get_ticks() - self.create_time > self.wait_time:
            return False
        else:
            # else it moves forward
            super().move(self.speed)
            for i in game.mob_mgr.enemies:
                if math.hypo(self.pos, i.pos) < 10:
                    i.change_health(-1)
                    return False
            return True


class MobManager:
    items = []
    enemies = []

    def __init__(self):
        pass

    def move_all(self):
        for i in self.items:
            if not i.exist():
                self.items.remove(i)

        for i in self.enemies:
            if not i.exist():
                self.enemies.remove(i)

    def new_mob(self, mob, *args):
        # decide if it is an enemy or item and add it to a list
        if mob is Enemy:
            self.enemies.append(mob(*args))
        else:
            self.items.append(mob(*args))

    def render(self, gameDisplay):
        for i in self.items:
            pygame.draw.circle(gameDisplay, i.colour, math.screen_pos(i.pos), i.size, 0)

        for e in self.enemies:
            pygame.draw.circle(gameDisplay, (255, 0, 0), math.screen_pos(e.pos), e.size, 0)
