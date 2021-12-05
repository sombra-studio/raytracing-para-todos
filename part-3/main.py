from PIL import Image
import numpy as np
# local modules
from camera import Camera
from light import PointLight
from render import render
from scene import Plane, Scene, Sphere


OUTPUT_FILENAME = "img.png"
MAX_COLOR_VALUE = 255


def main():
    # Create sphere
    sphere_pos = np.array([0, 0, 1.5])
    sphere_rad = 0.4
    color_purple = np.array([75 / MAX_COLOR_VALUE, 0, 130 / MAX_COLOR_VALUE])
    sphere = Sphere(sphere_pos, color_purple, sphere_rad)
    # Create plane
    plane_pos = np.array([0, -0.4, 0])
    color_gray = np.array([
        130 / MAX_COLOR_VALUE, 130 / MAX_COLOR_VALUE, 130 / MAX_COLOR_VALUE
    ])
    plane_n = np.array([0, 1, 0])
    plane = Plane(plane_pos, color_gray, plane_n)
    # Create Scene
    scene = Scene()
    scene.objects = [sphere, plane]
    # Create light
    light_pos = np.array([0, 1.5, 0])
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
    # Change this for lower or higher resolution
    pixel_scale = 15
    width = width_ratio * pixel_scale
    height = height_ratio * pixel_scale
    img_arr = render(scene, light, camera, height, width)
    img = Image.fromarray(img_arr)
    img.save(OUTPUT_FILENAME)
    print(f"Image saved in {OUTPUT_FILENAME}")


if __name__ == '__main__':
    main()
