import matplotlib.pyplot as plt
from numpy import ndarray


def make_histogram(img: ndarray) -> None:
    '''
    Make histogram of image
    :param img: image which will be process in histogram
    :return: None
    '''
    plt.hist(img.ravel(), 256, [0, 256])
    plt.xlabel("Тон пикселя")
    plt.ylabel("Частота")
    plt.show()
