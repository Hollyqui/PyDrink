import numpy as np
import matplotlib.pyplot as plt
from matplotlib import dates
import datetime
from factor_adjust import Adjustment
import pandas as pd
import matplotlib.dates as mdates


class Eliminator:

    def __init__(self, minute):
        self.minute = minute
        self.time_array = np.load("added_drinks.npy")
        self.elination_array = []
        self.eliminating = False
        try:
            self.elimination_rate = np.average(np.load("adjustment.npy"))
        except:
            self.elimination_rate = 0.018

    def elimination(self):
        if self.eliminating == False:
            elimination_array = []
            elimination_array.append(0)
            for i in range(1, len(self.time_array)):
                if self.time_array[i-1]-np.multiply(self.elimination_rate, np.divide(elimination_array,60))[i-1] > 0:
                    elimination_array.append(elimination_array[i-1]+1)
                else:
                    elimination_array.append(elimination_array[i-1])
            elimination_array = np.multiply(self.elimination_rate, np.divide(elimination_array,60))
            self.time_array = np.subtract(self.time_array, elimination_array)
            for i in range(len(self.time_array)):
                if self.time_array[i] < 0:
                    self.time_array[i] = 0
            self.eliminating = True
        np.save("eliminated_array", self.time_array)
    def plot(self):

        k = 1
        for i in reversed(range(1,len(self.time_array))):
            if self.time_array[i] != 0:
                k = i
                break
        # fig = plt.figure()
        # ax = fig.add_subplot(111)
        # ax.plot(self.time_array)
        # ax.yaxis_date()

        times = pd.date_range(start=0, periods=1440+self.minute, freq='1min')
        fig, ax = plt.subplots(1)
        fig.autofmt_xdate()
        plt.plot(times, self.time_array)
        # plt.xlim(right=k + 6, left=self.minute - 5)

        xfmt = mdates.DateFormatter('%H:%M')
        ax.xaxis.set_major_formatter(xfmt)
        plt.show()

        # plt.plot(self.time_array)

        # plt.ylabel('BAC')
        # plt.show()

    def load(self):
        self.elimination_array = np.load("elimination_array.npy")
        self.time_array = np.load("time_array.npy")
    def max_value(self):
        return np.max(self.time_array)
    def adjustment(self, sober_time):
        Adjustment.calc(max_value(), 0 , sober_time)



if __name__ == '__main__':
    eli = Eliminator(800)
    eli.adjustment(200)
    eli.elimination()
    eli.plot()