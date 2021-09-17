import numpy as np


def normalize(arr):
    norm = np.linalg.norm(arr)
    if norm == 0:
        return arr
    return arr / norm
