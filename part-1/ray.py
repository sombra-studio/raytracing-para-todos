import numpy as np


class Ray:
    def __init__(self, pr, nr):
        self.pr = pr
        self.nr = nr

    def intersect_sphere(self, sphere):
        pc = sphere.position
        diff = self.pr - pc
        b = np.dot(self.nr, diff)
        c = np.dot(diff, diff) - sphere.radius ** 2
        discriminant = b ** 2 - c
        if b > 0 or discriminant < 0:
            return None
        t = -1 * b - np.sqrt(discriminant)
        ph = self.pr + t * self.nr
        return ph
