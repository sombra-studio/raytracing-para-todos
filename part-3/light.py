import utils


class PointLight:
    def __init__(self, pos):
        self.position = pos

    def get_distance(self, p):
        """
        Get the distance between the given point and the position of the light
        Args:
            p(ndarray): A given point

        Returns:
            float: Distance between light position and point position
        """
        distance = utils.distance(self.position, p)
        return distance
