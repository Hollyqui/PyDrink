import numpy as np
from addition import Adder
from eliminator import Eliminator
name = input("What's your name?")
try:
    user_info = np.load(name+".npy")
    user_info = user_info.tolist()
    a = Adder(user_info[0][0], user_info[0][1])
    temp = []
    temp.append(int(input("How drunk do you feel?")))
    # temp.append(int(input("How full are you?")))
    time = input("What time is it? (enter in XX:YY format")
    hour = int((time[0]+time[1]))
    minute = int((time[3]+time[4]))
    minute += hour*60
    temp.append(minute)
    temp.append(int(input("How much % alcohol did your drink have?")))
    temp.append(int(input("How much ml of you drink did you have?")))
    user_info.append(temp)
    a.array(temp[3], temp[2], temp[1])
    a.plot()
    e = Eliminator()
    e.elimination()
    e.plot()
except:
    user_info = []
    temp = []
    temp.append(int(input("How tall are you?")))
    temp.append(int(input("How much do you weight?")))
    temp.append(int(input("How old are you?")))
    user_info.append(temp)
np.save(name+".npy", user_info)