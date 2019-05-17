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
from get_Image2 import get_image
import readchar

if os.path.isdir("Data") and os.path.isdir("Data/IMG"):
    pass
else:
    os.mkdir('Data')
    os.mkdir('Data/IMG')

def on_press(key):
    key = readchar.readkey()
    try:
        # print('alphanumeric key {0} pressed'.format(
        #     key.char))
        if key == 'w':
            print('Command forward ')
            get_image('http://192.168.1.95:8080/shot.jpg', False)
            # forward()
        elif key == 'a':
            print('Command left ')
            get_image('http://192.168.1.95:8080/shot.jpg', True)
            # i+=1
            # left()

        elif key == 's':
            print('Command backward ')
            get_image('http://192.168.1.95:8080/shot.jpg', False)
            # backward()
        elif key == 'd':
            print('Command right ')
            get_image('http://192.168.1.95:8080/shot.jpg', True)
            # right()

        elif key == 'a' and key == 'w':
            print('Command left-forward ')
            get_image('http://192.168.1.95:8080/shot.jpg', True)
            # left()
            # forward()

        elif key == 'd' and key == 'w':
            print('Command right-forward ')
            get_image('http://192.168.1.95:8080/shot.jpg', True)
            # right()
            # forward()


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

# if  key.char == 'd' or  key.char == 'a':
    buffer += '{}, {}, {},\n'.format(strftime("$%H$%M$%S", gmtime()), ti1, key)
    f.write(buffer)

    if key == keyboard.Key.esc:
        # Stop listener
        return False
    # stop()
    # write2csv('dob.csv', times )



i = 0
t = time.time()
f = open('Data/driving_log.csv', 'w')
f.write("{}, {}, {}, {}".format('Img', 'Current', 'Time', 'Key'))

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        # t = time.time()
    listener.join()
    # forward()
    # time.sleep(0.2)
    # stop()
    # time.sleep(0.4)