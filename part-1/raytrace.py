import numpy as np
import utils


RGB_CHANNELS = 3


def raytrace(ray, sphere, light):
    ph = ray.intersect_sphere(sphere)
    if ph is not None:
        n = sphere.normal_at(ph)
        l = utils.normalize(light.position - ph)
        diffuse_coef = np.dot(n, l)
        t = max(0, diffuse_coef)
        color = t * sphere.color
        return color
    else:
        return np.zeros(RGB_CHANNELS)
