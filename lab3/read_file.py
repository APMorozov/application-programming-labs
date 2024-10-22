import cv2
from numpy import ndarray


def read_file(path_to_file: str) -> ndarray:
    '''
    Read img to ndarray
    :param path_to_file: PATH to folder where image store
    :return: img ndarray
    '''
    img = cv2.imread(path_to_file)
    return img
