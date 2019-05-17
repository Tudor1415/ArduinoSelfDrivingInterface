
# Arduino_Serial.write(str.encode('l'))
# Arduino_Serial.write(str.encode('r'))
# Arduino_Serial.write(str.encode('f'))
# Arduino_Serial.write(str.encode('b'))

import serial
import time
from helpers import  *

Arduino_Serial = serial.Serial('com5',9600)
print (Arduino_Serial.readline())

def countSec(duration):
    finish = False
    time.sleep(duration)
    finish = True
    return finish

def forward_ai(duration):
    while True:
        Arduino_Serial.write(str.encode('f'))
        if countSec(duration):
            break
        else:
            continue

def backward_ai(duration):
    while True:
        Arduino_Serial.write(str.encode('b'))
        if countSec(duration):
            break
        else:
            continue

def left_ai(duration):
    while True:
        Arduino_Serial.write(str.encode('r'))
        if countSec(duration):
            break
        else:
            continue

def right_ai(duration):
    while True:
        Arduino_Serial.write(str.encode('l'))
        if countSec(duration):
            break
        else:
            continue

def stop_ai():
    Arduino_Serial.write(str.encode('o'))

def steer_angle_forward(angle):
    duration = deg2time(angle)
    if angle < 0:
        while True:
            Arduino_Serial.write(str.encode('f'))
            Arduino_Serial.write(str.encode('l'))
            if countSec(duration):
                break
            else:
                continue
    else:
        while True:
            Arduino_Serial.write(str.encode('f'))
            Arduino_Serial.write(str.encode('r'))
            if countSec(duration):
                break
            else:
                continue