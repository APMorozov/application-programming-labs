import pandas as pd

from args_parser import args_parser
from dataframe import read_file, calcWHC, sortbymaxWH, add_resolution, sort_by_resolution
from histogram import calc_hist




def main():
    pd.options.display.max_rows = None
    pd.options.display.max_columns = None

    csvFile = args_parser()

    try:
        data = read_file(csvFile)
        print('Start df\n', data)
    except Exception as ex:
        print("Read file error:", ex)

    try:
        dataWHC = calcWHC(data)
        print('df with width height and channels\n', dataWHC)
    except Exception as ex:
        print("Calc WHC error:", ex)

    try:
        sortedWHData = sortbymaxWH(dataWHC, 800, 900)
        print('Sorted df by max width and height\n', sortedWHData)
    except Exception as ex:
        print("Sort by WH error:", ex)

    try:
        dataWithRes = add_resolution(dataWHC)
        print('df with resolution\n', dataWHC)
    except Exception as ex:
        print("Add resolution Error:", ex)

    try:
        sortedResData = sort_by_resolution(dataWithRes)
        print('sorted df by resolution\n', dataWHC)
    except Exception as ex:
        print("sort by resolution error:", ex)
    try:
        calc_hist(sortedResData)
    except Exception as ex:
        print("Draw hist error:", ex)


if __name__ == "__main__":
    main()
