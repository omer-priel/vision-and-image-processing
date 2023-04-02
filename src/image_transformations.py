# images transformations

import numpy as np

import cv2

from src.image_math import convulsion

def shrink_image(img: np.ndarray, length: int, axis: int = 0) -> np.ndarray:
    fx = fy = length / img.shape[axis]
    return cv2.resize(img, None, fx=fx, fy=fy)


def normalize_image(img: np.ndarray, M: int = 255) -> np.ndarray:
    return img / M


def unormalize_image(img: np.ndarray, M: int = 255) -> np.ndarray:
    return (img * M).astype(int)


def blur_image(img: np.ndarray, K: int):
    conv = np.array([1/float(K**2)] * K**2).reshape((K, K))

    return convulsion(img, conv)
