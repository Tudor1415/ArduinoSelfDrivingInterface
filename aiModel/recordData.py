from pynput import keyboard
import time
# from helpers import *
import pandas as pd
import numpy as np
import os
from time import gmtime, strftime
# from helpers import forward, left, backward, right, stop
import urllib
import urllib.request
import cv2

if os.path.isdir("Data") and os.path.isdir("Data/IMG"):
    pass
else:
    os.mkdir('Data')
    os.mkdir('Data/IMG')
def on_press(key):
    try:
        # print('alphanumeric key {0} pressed'.format(
        #     key.char))
        if key.char == 'w':
            print('Command forward ')
            # forward()
        elif key.char == 'a':
            print('Command left ')
            # left()
        elif key.char == 's':
            print('Command backward ')
            # backward()
        elif key.char == 'd':
            print('Command right ')
            # right()

        else:
            print('Command non-recieved ')

    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    timeInit = time.time()

    times = []
    print('Released')
    # p = time.time()-(time.time() - t)
    ti1 = str(timeInit - t)[0:5] #converting float to str, slicing the float
    print("The key",key," is pressed for",ti1,'seconds')

    f = open('Data/driving_log.csv', 'r+')
    buffer = f.read()
    f.close()

    length = len(open("Data/driving_log.csv").readlines())
    f = open('Data/driving_log.csv', 'w')

    buffer += '{}, {}, {}\n'.format(strftime("%H:%M:%S", gmtime()), ti1, key)
    f.write(buffer)
    # stop()
    # write2csv('dob.csv', times )
    if key == keyboard.Key.esc:
        # Stop listener
        return False

url = 'http://192.168.1.95:8080/shot.jpg'
i = 0
t = time.time()
f = open('Data/driving_log.csv', 'w')
f.write("{}, {}, {}, {}".format('Current', 'Time', 'Key', 'Img'))

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        # t = time.time()
    listener.join()