import cv2
import matplotlib.pyplot as plt
from numpy import ndarray


def calc_histogram(img: ndarray) -> list:
    '''
    Calculation of histogram
    :param img: img which be conversed into histogram
    :return: list of ndarray. It is a histograms sorted by channels
    '''
    channels = cv2.split(img)
    if len(channels) == 3:
        histb = cv2.calcHist([img], [0], None, [256], [0, 256])
        histr = cv2.calcHist([img], [1], None, [256], [0, 256])
        histg = cv2.calcHist([img], [2], None, [256], [0, 256])
        hists = [histb, histr, histg]
        return hists
    if len(channels) == 1:
        histbin = cv2.calcHist([img], [0], None, [256], [0, 256])
        hists = [histbin]
        return hists


def make_histogram(hists: list) -> None:
    '''
    Make histogram of image
    :param hists: list of ndarray,which store histogram sorted by channels(b,r,g) or binary
    :return: None
    '''
    plt.xlabel("Тон пикселя")
    plt.ylabel("Частота")
    plt.title("Гистограмма изображения по каналам")
    if len(hists) == 3:
        plt.plot(hists[0], label='Blue channel', color='b')
        plt.plot(hists[1], label='Red channel', color='r')
        plt.plot(hists[2], label='Green channel', color='g')
    if len(hists) == 1:
        plt.plot(hists[0], label='Binary channel')
    plt.legend()
    plt.show()
