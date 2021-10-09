import numpy as np

# Local modules
from scene import Plane, Sphere

class Ray:
    def __init__(self, pr, nr):
        self.pr = pr
        self.nr = nr

    def at(self, t):
        p = self.pr + t * self.nr
        return p

    def intersect(self, scene_object):
        if isinstance(scene_object, Sphere):
            return self.intersect_sphere(scene_object)
        elif isinstance(scene_object, Plane):
            return self.intersect_plane(scene_object)
        else:
            raise Exception("Intersect function not implemented")

    def intersect_sphere(self, sphere):
        pc = sphere.position
        diff = self.pr - pc
        b = np.dot(self.nr, diff)
        c = np.dot(diff, diff) - sphere.radius ** 2
        discriminant = b ** 2 - c
        if b > 0 or discriminant < 0:
            return -1
        t = -1 * b - np.sqrt(discriminant)
        return t

    def intersect_plane(self, plane):
        n_dot = np.dot(self.nr, plane.n)
        if n_dot == 0:
            return -1
        t = np.dot(plane.position - self.pr, plane.n) / n_dot
        if t > 0:
            return t
        return -1
