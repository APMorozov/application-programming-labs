import cv2
import pandas as pd
from pandas import DataFrame
import numpy

pd.options.display.max_rows = None
pd.options.display.max_columns = None

def read_file(csvpath: str) -> DataFrame:
    data = pd.read_csv("annotation.csv", header=None, sep=",", encoding="cp1251")
    if len(data.columns) == 3:
        data.drop(0, axis=1, inplace=True)
        data.columns = ['curPath', 'absPath']
    else:
        data.columns = ['curPath', 'absPath']
    return data


def add_columnsWHC(data: DataFrame) -> DataFrame:
    data['weight'] = None
    data['height'] = None
    data['channels'] = None
    return data


def calcWHC(data: DataFrame):
    WHC = []
    for elm in data['absPath']:
        file = open(elm, 'rb+')
        bytes = bytearray(file.read())
        numpyarray = numpy.asarray(bytes, dtype=numpy.uint8)
        img = cv2.imdecode(numpyarray, cv2.IMREAD_UNCHANGED)
        subWHS = [img.shape[1], img.shape[0], img.shape[2]]
        WHC.append(subWHS)
    data2 = pd.DataFrame(WHC)
    data2.columns = ['weight', 'height', 'channels']
    resdata = pd.concat([data, data2], axis=1)
    return resdata


def sortbymaxWH(data: DataFrame, maxW: int, maxH: int) -> DataFrame:
    newdatatodf = []
    for i in range(len(data)):
        #print(data.at[i, 'weight'])
        if (data.at[i, 'weight'] <= maxW) and (data.at[i, 'height'] <= maxH):
            newdatatodf.append(data.iloc[i])
    newdata = pd.DataFrame(newdatatodf)
    return newdata


def add_resolution(data: DataFrame) -> DataFrame:
    resolution = []
    for i in range(len(data)):
        resolution.append(data.at[i, 'weight'] * data.at[i, 'height'])
    data2 = pd.DataFrame(resolution)
    data2.columns = ['resolution']
    resdata = pd.concat([data, data2], axis=1)
    return resdata


def sort_by_resolution(data: DataFrame) -> DataFrame:
    sorted_data = data.sort_values(by='resolution')
    return sorted_data
