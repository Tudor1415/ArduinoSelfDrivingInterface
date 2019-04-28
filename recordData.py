from pynput import keyboard
import time
from helpers import *
import pandas as pd
import numpy as np
import os
from time import gmtime, strftime

def on_press(key):
    try:
        # print('alphanumeric key {0} pressed'.format(
        #     key.char))
        if key.char == 'w':
            print('Command forward ')
        elif key.char == 'a':
            print('Command left ')
        elif key.char == 's':
            print('Command backward ')
        elif key.char == 'd':
            print('Command right ')
        else:
            print('Command non-recieved ')

    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    times = []
    print('Released')
    # p = time.time()-(time.time() - t)
    ti1 = str(time.time() - t)[0:5] #converting float to str, slicing the float
    print("The key",key," is pressed for",ti1,'seconds')

    f = open('driving_log.csv', 'r+')
    buffer = f.read()
    f.close()

    length = len(open("driving_log.csv").readlines())
    f = open('driving_log.csv', 'w')

    buffer += '{}, {}, {}\n'.format(strftime("%H:%M:%S", gmtime()), ti1, str(key))
    f.write(buffer)

    # write2csv('dob.csv', times )
    if key == keyboard.Key.esc:
        # Stop listener
        return False


t = time.time()
f = open('driving_log.csv', 'w')
f.write("{}, {}, {}".format('Current', 'Time', 'Key'))
# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        # t = time.time()
    listener.join()

calibTime('driving_log')




