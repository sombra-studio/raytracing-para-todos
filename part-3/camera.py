import numpy as np
import utils


class Camera:
    def __init__(self, pos, v_up, v_view, d, sx, sy):
        self.position = pos
        self.n0 = utils.normalize(np.cross(v_view, v_up))
        self.n1 = utils.normalize(np.cross(self.n0, v_view))
        self.n2 = utils.normalize(np.cross(self.n1, self.n0))
        pc = self.position + d * self.n2
        self.p00 = pc - (sx / 2) * self.n0 - (sy / 2) * self.n1
        self.d = d
        self.sx = sx
        self.sy = sy
