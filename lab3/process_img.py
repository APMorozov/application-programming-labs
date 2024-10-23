import cv2
from numpy import ndarray


def process2binary(img: ndarray) -> ndarray:
    '''
    Process img to binary
    :param img: img which will be process
    :return: binary image
    '''
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary_img = cv2.threshold(gray_img, 128, 192, cv2.THRESH_OTSU)
    return binary_img


def showimg(img: ndarray, name: str) -> None:
    '''
    Show image
    :param img: image which will show
    :param name: Name of header
    :return: None
    '''
    cv2.imshow(name, img)
    cv2.waitKey(0)
