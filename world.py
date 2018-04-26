class WorldManager:
    def __init__(self):
        self.caves = [Cave([500, 500], 50)]

    def add_cave(self, pos, radius):
        self.caves.append(Cave(pos, radius))

    def render(self):
        pass


class Cave:
    def __init__(self, pos, radius):
        self.pos = pos
        self.radius = radius
