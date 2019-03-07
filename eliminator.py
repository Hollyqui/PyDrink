import numpy as np
import matplotlib.pyplot as plt

class Eliminator:

    def __init__(self):
        self.time_array = np.load("added_drinks.npy")
        self.elination_array = []
        self.eliminating = False
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
        # while self.time_array[k] != 0:
        #     k += 1

        plt.plot(self.time_array)
        plt.xlim(right =k+6, left = -5 )
        plt.ylabel('BAC')
        plt.show()

    def load(self):
        self.elimination_array = np.load("elimination_array.npy")
        self.time_array = np.load("time_array.npy")


if __name__ == '__main__':
    eli = Eliminator()
    eli.elimination()
    eli.plot()