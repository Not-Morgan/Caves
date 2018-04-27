import pygame


class WorldManager:
    def __init__(self):
        self.caves = [Cave([500, 500], 50)]

    def add_cave(self, pos, radius):
        self.caves.append(Cave(pos, radius))

    def render(self, gameDisplay):
        for cave in self.caves:
            pygame.draw.circle(gameDisplay, (255, 255, 255), list(map(int, cave.pos)), cave.radius, 0)


class Cave:
    def __init__(self, pos, radius):
        self.pos = pos
        self.radius = radius
