import pygame
from random import randint
import extra_math as math
import game


class WorldManager:
    def __init__(self):
        self.caves = []
        self.cave_ends = []

    def render(self, gameDisplay):
        for cave in self.caves:
            pygame.draw.circle(gameDisplay, (255, 255, 255), math.screen_pos(cave[0]), cave[1], 0)

    def add_hole(self, pos, radius):
        new_cave = [pos, radius]
        self.caves.append(new_cave)
        # print("[*]", len(self.caves), self.caves)

    def make_cave(self, start_pos, size, length, direction=randint(0, 360)):
        if length == 0:
            self.cave_ends.append(start_pos)
            # print("[world gen] cave too short")
            return

        new_pos = [start_pos[0], start_pos[1]]
        new_pos[0] += math.cos(math.radians(direction)) * size * 0.75
        new_pos[1] += math.sin(math.radians(direction)) * size * 0.75

        if math.in_circles(new_pos, self.caves):
            # print("[world gen] cave collision len ", length)
            return

        self.add_hole([start_pos[0], start_pos[1]], size)
        if not randint(0, 70):
            game.mob_mgr.new_mob(Chest, start_pos,
                                 {"bombs": randint(1, 8), "points": randint(1, 8), "health": randint(0, 100)})
            # print("[world gen] new chest")

        # print("{}\n{}\n{}\n{}\n---------".format(start_pos, new_pos, length, direction))

        self.make_cave(new_pos, size, length - 1, direction + randint(-20, 20))
        if not randint(0, 15):
            new_dir = direction
            if randint(0, 1):
                new_dir += 90
            else:
                new_dir += -90

            new_pos[0] += math.cos(math.radians(new_dir)) * size * 0.9
            new_pos[1] += math.sin(math.radians(new_dir)) * size * 0.9

            self.make_cave(new_pos, size, length - 1, new_dir)
            # print("[world gen] new cave", length)

    #2C
    def generate_world(self):
        self.make_cave([500, 500], 25, 40)
        self.make_cave([0, 0], 25, 40)
        self.make_cave([1000, 0], 25, 40)
        self.make_cave([0, 1000], 25, 40)
        self.make_cave([1000, 1000], 25, 40)

        new_caves = self.cave_ends
        for i in new_caves:
            if randint(0, 1):
                self.make_cave(i, 25, 20)
            self.cave_ends.remove(i)

        # print("[world gen]", len(self.caves), "caves")
        # print("[world gen]", len([x for x in game.mob_mgr.items if isinstance(x, Chest)]), "chests")

    def extend_caves(self, pos):
        new_caves = self.cave_ends
        for i in [x for x in new_caves if math.hypo(x, pos) < 1000]:
            if randint(0, 2):
                self.make_cave(i, 25, 30)
            self.cave_ends.remove(i)


class Chest:
    colour = (165, 42, 42)
    size = 6

    def __init__(self, pos, loot):
        self.pos = pos
        self.loot = loot

    def exist(self):
        if math.hypo(self.pos, game.player.pos) < 10:
            game.player.add_bombs(self.loot["bombs"])
            game.player.add_points(self.loot["points"])
            game.player.change_health(self.loot["health"])
            return False
        return True
