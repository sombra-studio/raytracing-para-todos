from PIL import Image
import numpy as np
# local modules
from camera import Camera
from light import PointLight
from render import render
from sphere import Sphere


OUTPUT_FILENAME = "img.png"


def main():
    # Create sphere
    sphere_pos = np.array([0, 0, 1.5])
    sphere_rad = 0.4
    color_blue = np.array([0, 0, 1])
    sphere = Sphere(sphere_pos, sphere_rad, color_blue)
    # Create light
    light_pos = np.array([0, 2, 0])
    light = PointLight(light_pos)
    # Create camera
    camera_pos = np.array([0, 0, 0])
    v_up = np.array([0, 1, 0])
    v_view = np.array([0, 0, 1])
    d = 0.035
    width_ratio = 16
    height_ratio = 9
    aspect_ratio = width_ratio / height_ratio
    sy = d
    sx = sy * aspect_ratio
    camera = Camera(camera_pos, v_up, v_view, d, sx, sy)
    pixel_scale = 40
    width = width_ratio * pixel_scale
    height = height_ratio * pixel_scale
    img_arr = render(sphere, light, camera, height, width)
    img = Image.fromarray(img_arr)
    img.save(OUTPUT_FILENAME)
    print(f"Image saved in {OUTPUT_FILENAME}")


if __name__ == '__main__':
    main()
