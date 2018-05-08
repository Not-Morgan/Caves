import pygame
from random import randint
import extra_math as math


class WorldManager:
    def __init__(self):
        self.caves = []
        self.make_cave([500, 500], 25, 5)

    def render(self, gameDisplay):
        for cave in self.caves:
            pygame.draw.circle(gameDisplay, (255, 255, 255), list(map(int, cave.pos)), cave.radius, 0)

    def add_hole(self, pos, radius):
        self.caves.append(Cave(pos, radius))

    def make_cave(self, start_pos, size, length, direction=randint(0, 365)):
        if length == 0:
            return

        self.add_hole(start_pos, size + randint(-5, 5))

        new_pos = start_pos
        new_pos[0] += math.cos(math.radians(direction)) * 50
        new_pos[1] += math.sin(math.radians(direction)) * 50

        self.make_cave(new_pos, size, length - 1, direction + randint(-15, 15))


class Cave:
    def __init__(self, pos, radius=50):
        self.pos = pos
        self.radius = radius

    def __repr__(self):
        return "[{}, {}], {}".format(math.floor(self.pos[0]), math.floor(self.pos[1]), self.radius)
