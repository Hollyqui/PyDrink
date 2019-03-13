import numpy as np
from addition import Adder
from eliminator import Eliminator
import neural_network
import os

try:
    bac_array = np.load("bac_array.npy")
    bac_array = bac_array.tolist()
    user_input_array = np.load("user_input_array.npy")
    user_input_array = user_input_array.tolist()
    print("arrays loaded")
except:
    bac_array = []
    user_input_array = []
    print("arrays created")

name = input("Do you want to start a new drinking session? Y/n")
if name == "Y":
    try:
        os.remove("drinking_session.npy")
    except:
        None
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
    limit = input('Do you want to set a costume limit? (Y/N)')
    if limit == 'Y':
        limit = float(input('What is the max BAC you want to achieve?'))

    else:
        limit = -1
    temp.append(limit)
    user_info.append(temp)


elif name == "n":
    user_info = np.load("drinking_session.npy")
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
        elimination_array = np.load("eliminated_array.npy")
        elim_time = np.array(elimination_array[minute], ndmin=2)
        bac_array.append(elimination_array[minute])
        user_input_array.append(how_drunk)
        if len(bac_array) % 5 == 0:
            neural_network.learn(bac_array, user_input_array)
        if len(bac_array) == 1:
            neural_network.learn(bac_array, user_input_array)
        prediction = neural_network.predict(elim_time)
        print(prediction)


    elif decision == 2:
        sober_time = 0

        min = int(input("How many minutes ago did you sober up?"))
        sober_time = minute - min
        e.adjustment(sober_time)
    np.save("bac_array", bac_array)
    np.save("user_input_array", user_input_array)
np.save("drinking_session.npy", user_info)