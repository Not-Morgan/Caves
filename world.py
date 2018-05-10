import pygame
from random import randint
import extra_math as math
import game


class WorldManager:
    def __init__(self):
        self.caves = []

    def render(self, gameDisplay):
        for cave in self.caves:
            pygame.draw.circle(gameDisplay, (255, 255, 255), math.screen_pos(cave.pos), cave.radius, 0)

    def add_hole(self, pos, radius):
        new_cave = Cave(pos, radius)
        self.caves.append(new_cave)
        print("[*]", game.world_mgr.caves)

    def make_cave(self, start_pos, size, length, direction=randint(0, 365)):
        if length == 0:
            return

        self.add_hole(start_pos, size)

        new_pos = start_pos
        new_pos[0] += math.cos(math.radians(direction)) * 50
        new_pos[1] += math.sin(math.radians(direction)) * 50

        print("{}\n{}\n{}\n{}\n---------".format(start_pos, new_pos, length, direction))

        self.make_cave(new_pos, size, length - 1, direction + randint(-15, 15))

    def generate_world(self):
        self.make_cave([500, 500], 25, 5)
        print(self.caves)


class Cave:
    def __init__(self, pos, radius=50):
        self.pos = pos
        self.radius = radius

    def __repr__(self):
        return "[ [{}, {}], {}]".format(math.floor(self.pos[0]), math.floor(self.pos[1]), self.radius)
