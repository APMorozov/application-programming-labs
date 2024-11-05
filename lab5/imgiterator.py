import csv

class ImgIterator:
    def __init__(self, path_to_annotation: str):
        """
        Class constructor
        :param path_to_annotation: PATH to annotation where are store PATHs to images
        """
        self.path_to_annotation = path_to_annotation
        self.data = None  # Инициализируем data как None

    def __iter__(self):
        """
        data: stream of reading file
        reader: csv iterator
        :return:
        """
        self.data = open(self.path_to_annotation, 'r')
        self.reader = csv.reader(self.data)
        return self

    def __next__(self):
        """
        next obj
        """
        try:
            return next(self.reader)
        except StopIteration:
            self.data.close()
            raise StopIteration