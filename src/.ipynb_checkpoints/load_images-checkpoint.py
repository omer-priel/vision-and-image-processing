# load images

import os

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
