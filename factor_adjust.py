import numpy as np
class Adjustment:

    def calc(max_value, starting_time , sober_time):
        try:
            adjustment_array = np.load("adjustment.npy")
            adjustment_array = adjustment_array.tolist()
        except:
            adjustment_array = []

        adjustment = max_value/(sober_time/60-starting_time/60)



        adjustment_array.append(adjustment)
        np.save("adjustment.npy", adjustment_array)
        adjustment = np.average(adjustment_array)
        return adjustment

if __name__ == '__main__':
    print(Adjustment.calc(0.047, 0, 400))
