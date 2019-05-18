import serial
import win32api
import pygame
import sys
import time
from pynput.keyboard import Key, Controller

Arduino_Serial = serial.Serial('com5',9600)
print (Arduino_Serial.readline())

def left():
    Arduino_Serial.write(str.encode('l'))
    print ("left")

def right():
    Arduino_Serial.write(str.encode('r'))
    print ("right")

def forward():
    Arduino_Serial.write(str.encode('f'))
    print ("forward")


def backward():
    Arduino_Serial.write(str.encode('b'))
    print ("backward")



def stop():
    Arduino_Serial.write(str.encode('o'))
# right()
print ("Starting in .......")
n = 3
while n > 0:
    print(n)
    n -= 1
    time.sleep(1)

for i in range(0, 1):
    #######################
    #       Block 1       #
    #######################
    keyboard = Controller()
    right()
    for i in range(0, 2):
        keyboard.press('d')
        keyboard.press('w')
        right()
        forward()

        time.sleep(0.4)
        stop()
        keyboard.release('w')
        right()
        time.sleep(0.2)
        keyboard.release('d')
    stop()
    #######################
    #       Block 2       #
    #######################

    for i in range(0, 1):
        keyboard.press('a')
        keyboard.press('w')
        left()
        forward()
        time.sleep(0.3)
        stop()
        left()
        keyboard.release('w')
        time.sleep(0.3)
        keyboard.release('a')
    stop()
    #######################
    #       Block 3       #
    #######################
    for i in range(0, 2):
        right()
        forward()
        time.sleep(0.2)
        stop()
        right()
        time.sleep(0.3)
    stop()
    # #######################
    # #       Block 4       #
    # #######################
    forward()
    time.sleep(0.3)
    left()
    time.sleep(0.1)
    stop()
    for i in range(0, 1):
        keyboard.press('d')
        keyboard.press('w')
        right()
        forward()
        time.sleep(0.31)
        keyboard.release('w')
        stop()
        right()
        time.sleep(0.52)
        keyboard.release('d')
    stop()
    #######################
    #       Block 5       #
    #######################
    left()
    forward()
    time.sleep(0.15)
    stop()
    forward()
    time.sleep(0.55)
    stop()
    forward()
    right()
    time.sleep(0.4)
    stop()
    right()
    time.sleep(0.2)
    stop()
    forward()
    time.sleep(0.1)
    stop()
    # #######################
    # #       Block 6       #
    # #######################
    # for i in range(0, 1):
    #     keyboard.press('d')
    #     keyboard.press('w')
    #     right()
    #     forward()
    #     time.sleep(0.2)
    #     keyboard.release('w')
    #     stop()
    #     # right()
    #     time.sleep(0.4)
    #     keyboard.release('d')
    # stop()
    # #######################
    # #       Block 7       #
    # #######################
    # right()
    # forward()
    # time.sleep(0.2)
    # stop()
    # #######################
    # #       Block 8       #
    # #######################
    # right()
    # forward()
    # time.sleep(0.4)
    # stop()
    # #######################
    # #       Block 9       #
    # #######################
    # right()
    # forward()
    # time.sleep(0.4)
    # stop()
    # #######################
    # #       Block 10      #
    # #######################