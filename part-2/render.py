import numpy as np
from progress.bar import Bar

# local modules
from ray import Ray
from raytrace import raytrace
import utils

MAX_COLOR = 255
RENDERING_MSG = "Rendering"
RGB_CHANNELS = 3


def render(scene, light, camera, height, width):
    output = np.zeros([height, width, RGB_CHANNELS], dtype=np.uint8)
    total_count = height * width
    bar = Bar(
        RENDERING_MSG,
        max=total_count,
        suffix='%(percent)d%% [%(elapsed_td)s / %(eta_td)s]',
        check_tty=False
    )
    for j in range(height):
        for i in range(width):
            xp = (i / width) * camera.sx
            # we use height - 1 as the first value for y, because images
            # start at the top pixel row
            yp = ((height - 1 - j) / height) * camera.sy
            pp = camera.p00 + xp * camera.n0 + yp * camera.n1
            npe = utils.normalize(pp - camera.position)
            ray = Ray(pp, npe)
            color = raytrace(ray, scene, light)
            output[j][i] = np.round(color * MAX_COLOR)
            bar.next()
    bar.finish()
    return output
