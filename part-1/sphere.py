class Sphere:
    def __init__(self, pos, radius, color):
        self.position = pos
        self.radius = radius
        self.color = color

    def normal_at(self, p):
        n = (p - self.position) / self.radius
        return n
