import numpy as np
# local modules
from ray import Ray
from raytrace import raytrace
import utils


RGB_CHANNELS = 3
MAX_COLOR = 255


def render(sphere, light, camera, height, width):
    output = np.zeros([height, width, RGB_CHANNELS], dtype=np.uint8)
    for j in range(height):
        for i in range(width):
            xp = (i / width) * camera.sx
            # we use height - 1 as the first value for y, because images
            # start at the top pixel row
            yp = ((height - 1 - j) / height) * camera.sy
            pp = camera.p00 + xp * camera.n0 + yp * camera.n1
            npe = utils.normalize(pp - camera.position)
            ray = Ray(pp, npe)
            color = raytrace(ray, sphere, light)
            output[j][i] = np.round(color * MAX_COLOR)
    return output
