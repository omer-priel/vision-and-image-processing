# load images

import os
import numpy as np
import cv2

from src.config import DATASETS_PATH

# globals
datasetName: str = ""


def get_file_path(dataset: str, subpath: str = ".") -> str:
    return os.path.abspath(os.path.join(DATASETS_PATH, dataset + "/" + subpath))


def set_database(dataset: str) -> None:
    global datasetName
    datasetName = dataset


def get_dataset() -> str:
    return datasetName


def get_dataset_path(subpath: str = ".") -> str:
    return get_file_path(datasetName, subpath)


def load_image(subpath: str) -> tuple[np.ndarray, np.ndarray]:
    img_path = get_dataset_path(subpath)
    
    colored_img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    colored_img = cv2.cvtColor(colored_img, cv2.COLOR_BGR2RGB)
    
    gray_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    gray_img = cv2.cvtColor(gray_img, cv2.COLOR_BGR2RGB)
    
    return colored_img, gray_img
