# images transformations

import numpy as np
import cv2

def shrink_image(img: np.ndarray, length: int, axis: int = 0) -> np.ndarray:
    fx = fy = length / img.shape[axis]
    return cv2.resize(img, None, fx=fx, fy=fy)


def normalize_image(img: np.ndarray, N: int = 255) -> np.ndarray:
    return img / N


def unormalize_image(img: np.ndarray, N: int = 255) -> np.ndarray:
    return np.floor(img * N)
