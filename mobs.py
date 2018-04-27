import pygame
import extra_math as math
import game


class Mob:
    direction = 0
    speed = 1

    def __init__(self, pos):
        self.pos = pos

    def move(self, dist=None):
        if dist is None:
            dist = self.speed

        # move based on direction
        self.pos[0] += math.cos(math.radians(self.direction)) * dist
        self.pos[1] += math.sin(math.radians(self.direction)) * dist

        # undo if you went into a wall
        if not math.in_circles(self.pos, game.game_mgr.world_mgr.caves):
            self.pos[0] -= math.cos(math.radians(self.direction)) * dist
            self.pos[1] -= math.sin(math.radians(self.direction)) * dist

    def rotate(self, degrees):
        self.direction = (self.direction + degrees) % 360


# TODO enemies
class Enemy(Mob):
    pass


class Player(Mob):
    bombs = []

    def __init__(self, pos):
        super().__init__(pos)

    def throw_bomb(self):
        game.game_mgr.mob_mgr.new_mob(Bomb, [self.pos[0], self.pos[1]], self.direction)


class Bomb(Mob):
    wait_time = 1000
    radius = 25

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
        game.game_mgr.world_mgr.add_cave(self.pos, self.radius)


# TODO
class Bullet(Mob):
    pass


class MobManager:
    items = []
    enemies = []

    def __init__(self):
        pass

    def move_all(self):
        for i in self.items:
            if not i.exist():
                self.items.remove(i)

    def new_mob(self, mob, *args):
        if mob is Enemy:
            self.enemies.append(mob(*args))
        else:
            self.items.append(mob(*args))

    def render(self, gameDisplay):
        for i in self.items:
            pygame.draw.circle(gameDisplay, (0, 0, 255), list(map(int, i.pos)), 4, 0)

        for e in self.enemies:
            pygame.draw.circle(gameDisplay, (255, 0, 0), list(map(int, e.pos)), 4, 0)
