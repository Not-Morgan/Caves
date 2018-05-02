import pygame
from random import randint
import extra_math


class WorldManager:
    def __init__(self):
        self.caves = [Cave([500, 500], 50)]
        self.make_cave([500, 500], 5)

    def render(self, gameDisplay):
        for cave in self.caves:
            pygame.draw.circle(gameDisplay, (255, 255, 255), list(map(int, cave.pos)), cave.radius, 0)

    def add_hole(self, pos, radius):
        self.caves.append(Cave(pos, radius))

    def make_cave(self, start, length, start_dir=randint(0, 360)):
        pos = start
        direction = start_dir

        for i in range(length):
            self.add_hole(pos, 50)



class Cave:
    def __init__(self, pos, radius=50):
        self.pos = pos
        self.radius = radius
