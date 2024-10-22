import cv2
import os

from args_parser import arg_parser
from make_histogram import make_histogram
from process_img import process2binary, showimg
from read_file import read_file


def main():
    path_to_image, path_to_folder = arg_parser()
    try:
        img = read_file(path_to_image)
    except ProcessLookupError:
        print("Ошибка чтения файла")
    try:
        make_histogram(img)
    except Exception:
        print("Ошибка построения гистограммы")
    try:
        binary_img = process2binary(img)
    except ProcessLookupError:
        print("Ошибка обработки изображения в бинарное")
    showimg(img, "Start img")
    showimg(binary_img, "Binary img")
    print(os.path.join(path_to_folder, "result.jpg"))
    cv2.imwrite(os.path.join(path_to_folder, "result.jpg"), binary_img)


if __name__ == "__main__":
    main()
