---
layout: default
title: Raytracing para todos - Parte 3
---

[volver](..)

# Parte 3

Ahora veremos cómo crear sombras. Para esto hay que seguir el mismo sistema 
anterior en que disparamos rayos desde la cámara, obtenemos la primera 
intersección con un objeto y calculamos el color para ese punto, el que 
luego será asignado al pixel correspondiente. Lo normal es que cuando hay 
una sombra uno ve una pequeña parte del color de la superficie y otra buena 
parte de oscuridad. La oscuridad se debe a la ausencia de luz, y esta se 
produce cuando hay un objeto tapando el camino entre la superficie y la 
fuente de luz. La siguiente imagen puede ayudar a ilustrar este concepto:

[oclusion]

Lo que debemos hacer entonces para saber si existe un objeto ocluyendo la 
superficie, es:

1. Disparar un rayo desde el punto de intersección en la superficie, en 
   dirección a la fuente de luz
2. Para el resto de los objetos, verificar si este nuevo rayo los intersecta.
3. Si la intersección ocurre en el segmento entre el punto de la superficie 
   y la fuente de luz, entonces el punto tiene sombra. De lo contrario, el 
   objeto no está ocluyendo la luz.

[intersección sin oclusion]

Este es el código que necesitarías cambiar en la función *raytrace*:

```python
import numpy as np
import utils


# Local imports
from ray import Ray

COLOR_CHANNELS = 3
SHADOW_COLOR = np.zeros(COLOR_CHANNELS)


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
        color = diffuse_coef * hit_obj.color if not occlusion else SHADOW_COLOR
        return color
    else:
        return np.zeros(COLOR_CHANNELS)
```

Además para poder calcular distancia en la clase Light, modifica el archivo 
*light.py*:

```python
import utils


class PointLight:
    def __init__(self, pos):
        self.position = pos

    def get_distance(self, p):
        distance = utils.distance(self.position, p)
        return distance
```

Y en *utils.py* agrega:

```python
def distance(p1, p2):
    dist = np.linalg.norm(p1 - p2)
    return dist
```

[volver](..)
