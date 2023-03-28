# images math operations

import numpy as np

def image_histogram(img: np.ndarray, N: int = 255) -> np.ndarray:
    hist, colors = np.histogram(img, bins=np.arange(N + 2) - 0.5)
    colors = colors[:N+1] + 0.5
    return hist, colors

def image_histogram_channels(img: np.ndarray, N: int = 255) -> np.ndarray:
    histR, colorsR = np.histogram(img[:,:,0], bins=np.arange(N + 2) - 0.5)
    colorsR = colorsR[:N+1] + 0.5
    
    histG, colorsG = np.histogram(img[:,:,1], bins=np.arange(N + 2) - 0.5)
    colorsG = colorsG[:N+1] + 0.5
    
    histB, colorsB = np.histogram(img[:,:,2], bins=np.arange(N + 2) - 0.5)
    colorsB = colorsB[:N+1] + 0.5
    
    return histR, colorsR, histG, colorsG, histB, colorsB
