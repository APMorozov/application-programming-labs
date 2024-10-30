from dataframe import read_file, add_columnsWHC, calcWHC, sortbymaxWH, add_resolution, sort_by_resolution


def main():
    data = read_file("annotation.csv")

    data2 = calcWHC(data)
    sortbymaxWH(data2, 800, 900)
    data3 = add_resolution(data2)
    sort_by_resolution(data3)


if __name__ == "__main__":
    main()
