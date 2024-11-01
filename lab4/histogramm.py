import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import pandas as pd


def calc_hist(data: pd.DataFrame) -> None:
    '''
    Calc and draw hist
    :param data: DataFrame
    :return: None
    '''
    plt.figure(figsize=(10, 6))
    plt.xlabel("Resolution")
    plt.ylabel("Frequency")
    plt.title("Distribution of resolution")
    ax = plt.gca()
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    plt.xlim(0, 8500000)
    plt.hist([data["resolution"]], bins=len(data))
    plt.show()
