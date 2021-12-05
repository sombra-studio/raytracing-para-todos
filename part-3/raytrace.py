import numpy as np
import utils


# Local imports
from ray import Ray

COLOR_CHANNELS = 3
SHADOW_COLOR = np.zeros(COLOR_CHANNELS)
AMBIENT_LIGHT = np.ones(COLOR_CHANNELS) * 0.16


def get_min_intersection(ray, objects):
    min_t = np.inf
    hit_obj = None
    # Get first hit with an object by checking intersection with all objects
    for scene_object in objects:
        t = ray.intersect(scene_object)
        if 0 < t < min_t:
            hit_obj = scene_object
            min_t = t
    return min_t, hit_obj


def calculate_occlusion(ray, obj, light, objects):
    """
    Calculate if there is an object between the light and object
    Args:
        ray: A ray starting in the hit point with direction to the light
        obj: The object where the hit point is
        light: A source of light to calculate if it's occluded
        objects: The objects in the scene

    Returns:
        bool: If there is an occlusion or not
    """
    # Check for occlusion
    # 1. Shoot ray from point to light
    # 2. Check collision with other objects
    # 3. If there is one between the hit point and the light, there is occlusion
    light_distance = light.get_distance(ray.pr)
    for other_obj in objects:
        if other_obj == obj:
            continue
        shadow_t = ray.intersect(other_obj)
        if 0 < shadow_t <= light_distance:
            return True
    return False


def raytrace(ray, scene, light):
    min_t, hit_obj = get_min_intersection(ray, scene.objects)
    if hit_obj is not None:
        ph = ray.at(min_t)
        n = hit_obj.normal_at(ph)
        l = utils.normalize(light.position - ph)
        diffuse_coef = np.dot(n, l)
        diffuse_coef = np.clip(diffuse_coef, 0, 1)
        shadow_ray = Ray(ph, l)
        occlusion = calculate_occlusion(
            shadow_ray, hit_obj, light, scene.objects
        )
        if not occlusion:
            diffuse_color = diffuse_coef * hit_obj.color
        else:
            diffuse_color = SHADOW_COLOR
        ambient_color = AMBIENT_LIGHT * hit_obj.color
        color =  np.clip(diffuse_color + ambient_color, 0, 1)
        return color
    else:
        return np.zeros(COLOR_CHANNELS)
