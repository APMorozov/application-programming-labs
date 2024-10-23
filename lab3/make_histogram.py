import cv2
import matplotlib.pyplot as plt
from numpy import ndarray


def make_histogram(img: ndarray) -> None:
    '''
    Make histogram of image
    :param img: image which will be process in histogram
    :return: None
    '''
    channels = cv2.split(img)
    plt.xlabel("Тон пикселя")
    plt.ylabel("Частота")
    plt.title("Гистограмма изображения по каналам")
    if len(channels) == 3:
        hist1 = cv2.calcHist([img], [0], None, [256], [0, 256])
        plt.plot(hist1,label='Blue channel', color='b')
        hist2 = cv2.calcHist([img], [1], None, [256], [0, 256])
        plt.plot(hist2, label='Red channel', color='r')
        hist3 = cv2.calcHist([img], [2], None, [256], [0, 256])
        plt.plot(hist3, label='Green channel', color='g')
    if len(channels) == 1:
        hist1 = cv2.calcHist([img], [0], None, [256], [0, 256])
        plt.plot(hist1, label='Binary channel')
    plt.legend()
    plt.show()
