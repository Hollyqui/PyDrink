import matplotlib.pyplot as plt
import numpy as np
class calc:
    def __init__(self):
        self.time_array = []

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

    # def elimination(self, time_array, elimination_rate):
    #     count = 0
    #     for i in range(len(time_array)):
    #         if time_array[i] > 0:
    #             self.time_array[i] -= (elimination_rate * ((i-count) / 60))
    #         else:
    #             count = i
    #         if self.time_array[i] < 0:
    #             self.time_array[i] = 0
    def elimination(self, time_array, elimination_rate):
        elimination_array = []
        elimination_array.append(0)
        for i in range(1, len(time_array)):
            if time_array[i-1]-np.multiply(elimination_rate, np.divide(elimination_array,60))[i-1] > 0:
                elimination_array.append(elimination_array[i-1]+1)
            else:
                elimination_array.append(elimination_array[i-1])
        print(elimination_array)
        elimination_array = np.multiply(elimination_rate, np.divide(elimination_array,60))
        self.time_array = np.subtract(time_array, elimination_array)


    def array(self, volume, percent, time):
        minutes = -time
        weight = 70
        height = 170
        gender = True
        half_life = 18
        temp_time_array = []
        while len(temp_time_array)<400: #self.time_array[len(self.time_array)-1] < 0.001:
            abs_alc = self.drink(volume, percent, minutes, half_life)
            temp_time_array.append(self.bac_calc(abs_alc, self.widmark(weight, height, gender), weight))
            minutes += 1
        if len(self.time_array) == 0:
            self.time_array = temp_time_array
        else: self.time_array = np.add(self.time_array, temp_time_array)
    def main(self, elimination_rate):
        #None
        self.elimination(self.time_array, elimination_rate)

if __name__ == '__main__':
    test = calc()
    volume = 330
    percent = 10
    elimination_rate = 0.018
    test.array(volume, percent, 0)
    test.array(volume, percent, 50)
    test.array(volume, percent, 100)
    test.main(elimination_rate)
    plt.plot(test.time_array)
    plt.ylabel('some numbers')
    plt.show()
