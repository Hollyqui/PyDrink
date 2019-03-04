import matplotlib.pyplot as plt
import numpy as np


class Calculator:
    def __init__(self):
        self.time_array = []
        self.eliminating = False
        self.elimination_rate = 0.018

    #find the widmark factor
    def widmark(self, weight, height, gender):
        BMI = weight/pow((height/100),2)
        if gender:
            male_r = 1.0181 -0.01213 * BMI
            return male_r
        else:
            female_r = 0.9367 - 0.01240 * BMI
            return female_r

    #finds how much alcohol of each drink is absorbed at each time
    def drink(self, volume, percent, minutes, half_life):
        half_lifes_passed = minutes/half_life
        alcohol = (volume/1000)*(percent/100)- (volume/1000)*(percent/100) * pow(0.5, half_lifes_passed)
        return alcohol

    def bac_calc(self,alcohol, widmark_factor, weight):
        density = 0.78974
        C = (100 * alcohol * density) / (widmark_factor * weight)
        if C < 0: return 0
        else: return C

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


    def array(self, volume, percent, time):
        minutes = -time
        weight = 70
        height = 193
        gender = True
        half_life = 12
        temp_time_array = []
        while len(temp_time_array)<500: #self.time_array[len(self.time_array)-1] < 0.001:
            abs_alc = self.drink(volume, percent, minutes, half_life)
            temp_time_array.append(self.bac_calc(abs_alc, self.widmark(weight, height, gender), weight))
            minutes += 1
        if len(self.time_array) == 0:
            self.time_array = temp_time_array
        else: self.time_array = np.add(self.time_array, temp_time_array)
    def main(self, volume, percent, time):
        self.array(volume, percent, time)
    def plot(self):
        self.elimination()
        plt.plot(self.time_array)
        plt.ylabel('BAC')
        plt.show()


