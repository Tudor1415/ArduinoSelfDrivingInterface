import serial
import win32api
import pygame
import sys
import time
from pynput.keyboard import Key, Controller

Arduino_Serial = serial.Serial('com5',9600)
print (Arduino_Serial.readline())
print ("Starting in .......")
n = 3
while n > 0:
    print(n)
    n -= 1
    time.sleep(1)

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

# for i in range(0,4):
#     left()
#     forward()
#     time.sleep(0.32)
#     stop()
#     time.sleep(0.02)

# left()
# forward()
# time.sleep(0.2)
# right()
# forward()
# time.sleep(0.35)
# stop()
# # left()
# right()
# time.sleep(1)
# forward()
# time.sleep(0.25)
# # stop()
# # right()
# # forward()
# # time.sleep(1.5)
# # stop()
# # right()
# stop()



# for i in range(0, 20):
#     forward()
#     time.sleep(0.1)
# right()
# keyboard = Controller()
# for i in range(0, 20):

#     for i in range(0, 4):
#         keyboard.press('d')
#         keyboard.press('w')
#         # right()
#         left()
#         forward()
#         time.sleep(0.175)
#         stop()
#         keyboard.release('w')
#         # right()
#         left()
#         time.sleep(0.3)
#         keyboard.release('d')
#         # forward()
#         # time.sleep(0.1)
#         # stop()

# stop()

# stop()
# keyboard.press('esc')
# keyboard.release('esc')


#####################################################
right()
for i in range(0, 3):
    right()
    forward()
    time.sleep(0.3)
    stop()
    right()
    time.sleep(0.75)
stop()
left()
forward()
time.sleep(0.2)
stop()
left()
time.sleep(0.75)
stop()
