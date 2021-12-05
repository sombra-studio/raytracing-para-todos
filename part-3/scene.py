class Scene:
    def __init__(self):
        """
        A scene has multiple SceneObject
        """
        self.objects = []


class SceneObject:
    def __init__(self, pos, color):
        """
        Object that belongs to a scene
        Args:
            pos(ndarray): Position in 3D space
            color(ndarray): Color in 3 channels using float 0 to 1
        """
        self.position = pos
        self.color = color

    def normal_at(self, p):
        """
        Get the normal at point p
        Args:
            p(ndarray): A point in the surface of the object

        Returns:
            ndarray: The normal at the given point
        """
        pass


class Sphere(SceneObject):
    def __init__(self, pos, color, radius):
        SceneObject.__init__(self, pos, color)
        self.radius = radius

    def normal_at(self, p):
        n = (p - self.position) / self.radius
        return n


class Plane(SceneObject):
    def __init__(self, pos, color, n):
        """
        Object that belongs to a scene
        Args:
            pos(ndarray): Position in 3D space
            color(ndarray): Color in 3 channels using float 0 to 1
            n(ndarray): Normal of the plane as a 3D vector
        """
        SceneObject.__init__(self, pos, color)
        self.n = n

    def normal_at(self, p):
        return self.n
