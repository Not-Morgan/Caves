import math
from extra_math import *


# TODO mob manager
class MobManager:
    def __init__(self):
        pass

    def move_all(self):
        pass

    def spawn_mob(self):
        pass

    def render(self):
        pass


class Mob:
    direction = 0
    speed = 1

    def __init__(self, pos):
        self.pos = pos

    def move(self, dist=None):
        if dist is None:
            dist = self.speed

        self.pos[0] += math.cos(math.radians(self.direction)) * dist
        self.pos[1] += math.sin(math.radians(self.direction)) * dist
        
        # TODO make work with cave list from WorldManager
        if not any([hypo(self.pos, c[0]) < c[1] for c in [[(500, 500), 50]]]):
            self.pos[0] -= math.cos(math.radians(self.direction)) * dist
            self.pos[1] -= math.sin(math.radians(self.direction)) * dist

    def rotate(self, degrees):
        self.direction = (self.direction + degrees) % 360


# TODO enemies
class Enemy(Mob):
    pass


class Player(Mob):
    def __init__(self, pos):
        super().__init__(pos)
