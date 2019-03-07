import numpy as np
from addition import Adder
from eliminator import Eliminator


name = input("What's your name?")

try:
    user_info = np.load(name+".npy")
    user_info = user_info.tolist()
    a = Adder(user_info[0][0], user_info[0][1], user_info[0][3])
    temp = []
    decision = int(input("choose an option: 1. to add a drink 2. to say that you are sober"))

    if decision == 1:
        # temp.append(int(input("How full are you?")))
        time = input("What time is it? (enter in XX:YY format")
        hour = int((time[0]+time[1]))
        minute = int((time[3]+time[4]))
        minute += hour*60
        temp.append(minute)
        how_drunk = int(input("How drunk do you feel?"))

        temp.append(how_drunk)
        temp.append(int(input("How much % alcohol did your drink have?")))
        temp.append(int(input("How much ml of you drink did you have?")))
        user_info.append(temp)
        a.array(temp[3], temp[2], temp[0])
        a.plot()

        e = Eliminator(user_info[0][3])
        e.elimination()
        e.plot()
    elif decision == 2:
        sober_time = 0

        min = int(input("How many minutes ago did you sober up?"))
        sober_time = minute - min
        e.adjustment(sober_time)

except:
    user_info = []
    temp = []
    temp.append(int(input("How tall are you?")))
    temp.append(int(input("How much do you weight?")))
    temp.append(int(input("How old are you?")))
    time = input("What is the time that you started drinking? (enter in XX:YY format)")
    hour = int((time[0] + time[1]))
    minute = int((time[3] + time[4]))
    minute += hour * 60
    temp.append(minute)
    user_info.append(temp)
np.save(name+".npy", user_info)