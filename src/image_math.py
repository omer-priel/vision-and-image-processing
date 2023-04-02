# images math operations

import numpy as np
import scipy

def image_histogram(img: np.ndarray, M: int = 255) -> np.ndarray:
    hist, colors = np.histogram(img, bins=np.arange(M + 2) - 0.5)
    colors = colors[:M+1] + 0.5
    return hist, colors


def image_histogram_channels(img: np.ndarray, M: int = 255) -> np.ndarray:
    histR, colorsR = image_histogram(img[:,:,0], M)
    histG, colorsG = image_histogram(img[:,:,1], M)
    histB, colorsB = image_histogram(img[:,:,2], M)

    return histR, colorsR, histG, colorsG, histB, colorsB


def convulsion(img: np.ndarray, conv: np.ndarray):
    newImg = np.empty(img.shape)

    for dim in range(3):
        newImg[:,:,dim] = scipy.signal.convolve2d(img[:,:,dim], conv, boundary='symm', mode='same')

    return newImg
