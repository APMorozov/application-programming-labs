import pandas as pd

from args_parser import args_parser
from dataframe import read_file, calcWHC, sortbymaxWH, add_resolution, sort_by_resolution, get_static
from histogramm import calc_hist




def main():
    pd.options.display.max_rows = None
    pd.options.display.max_columns = None
    try:
        csvFile = args_parser()

        data = read_file(csvFile)
        print('Start df\n', data)

        dataWHC = calcWHC(data)
        print('df with width height and channels\n', dataWHC)


        sortedWHData = sortbymaxWH(dataWHC, 1000, 1000)
        print('Sorted df by max width and height\n', sortedWHData)

        dataWithRes = add_resolution(dataWHC)
        print('df with resolution\n', dataWHC)

        sortedResData = sort_by_resolution(dataWithRes)
        print('sorted df by resolution\n', dataWHC)
        calc_hist(sortedResData)
        print("Statistic Data:")
        get_static(dataWithRes)
    except Exception as ex:
        print('Error:', ex)



if __name__ == "__main__":
    main()
