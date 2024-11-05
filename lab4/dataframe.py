import cv2
from pandas import DataFrame
import pandas as pd


def read_file(csvpath: str) -> DataFrame:
    '''
    Read data to dataframe from csv file
    :param csvpath: path to csv file whit curPath and absPath
    :return: DataFrame with 2 columns curPath and absPath
    '''
    data = pd.read_csv("annotation.csv", header=None, sep=",", encoding="cp1251")
    if len(data.columns) == 3:
        data.drop(0, axis=1, inplace=True)
        data.columns = ['curPath', 'absPath']
    else:
        data.columns = ['curPath', 'absPath']
    return data


def calcWHC(data: DataFrame) -> DataFrame:
    '''
    Add and calc 3 columns width, height and channels
    :param data: DataFrame with 2 columns
    :return: DataFrame with width, height and channels
    '''
    WHC = []
    for elm in data['absPath']:
        img = cv2.imread(elm)
        subWHS = [img.shape[1], img.shape[0], img.shape[2]]
        WHC.append(subWHS)
    data2 = pd.DataFrame(WHC)
    data2.columns = ['width', 'height', 'channels']
    resdata = pd.concat([data, data2], axis=1)
    return resdata


def sortbymaxWH(data: DataFrame, maxW: int, maxH: int) -> DataFrame:
    '''
    Sort DataFrame by max width and height
    :param data: DataFrame
    :param maxW: max width
    :param maxH: max height
    :return: sorted DataFrame
    '''
    sortdata = data.copy(deep=True)[(data['width'] < maxW) & (data['height'] < maxH)]
    return sortdata


def get_static(data: DataFrame) -> None:
    '''
    Print statics width, height and channels
    :param data: DataFrame
    :return: None
    '''
    print(data['width'].describe())
    print(data['height'].describe())
    print(data['channels'].describe())



def add_resolution(data: DataFrame) -> DataFrame:
    '''
    add resolution
    :param data: DataFrame with width and height columns
    :return: DataFrame with resolution
    '''
    data['resolution'] = (data['width'] * data['height'])
    return data


def sort_by_resolution(data: DataFrame) -> DataFrame:
    '''
    Sort be resolution.Min to max resolution
    :param data: DataFrame
    :return: sorted DataFrame
    '''
    sorted_data = data.sort_values(by='resolution')
    return sorted_data
