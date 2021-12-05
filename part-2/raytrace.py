import numpy as np
import utils


RGB_CHANNELS = 3


def raytrace(ray, scene, light):
    min_t = np.inf
    hit_obj = None
    for scene_object in scene.objects:
        t = ray.intersect(scene_object)
        if t > 0 and t < min_t:
            hit_obj = scene_object
            min_t = t
    if hit_obj is not None:
        ph = ray.at(min_t)
        n = hit_obj.normal_at(ph)
        l = utils.normalize(light.position - ph)
        diffuse_coef = np.dot(n, l)
        t = max(0, diffuse_coef)
        color = t * hit_obj.color
        return color
    else:
        return np.zeros(RGB_CHANNELS)
