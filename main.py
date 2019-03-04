import numpy as np
from calc import Calculator

name = input("What's your name?")
c = Calculator()
try:
    user_info = np.load(name+".npy")
    user_info = user_info.tolist()
    temp = []
    temp.append(int(input("How drunk do you feel?")))
    temp.append(int(input("How full are you?")))
    time = input("What time is it? (enter in XX:YY format")
    hour = int((time[0]+time[1]))
    minute = int((time[3]+time[4]))
    minute += hour*60
    temp.append(minute)
    temp.append(int(input("How much % alcohol did your drink have?")))
    temp.append(int(input("How much ml of you drink did you have?")))
    user_info.append(temp)
    for i in range(1, len(user_info)):
        c.main(user_info[i][4], user_info[i][3], user_info[i][2])
    c.plot()
except:
    user_info = []
    temp = []
    temp.append(int(input("How tall are you?")))
    temp.append(int(input("How much do you weight?")))
    temp.append(int(input("How old are you?")))
np.save(name+".npy", user_info)