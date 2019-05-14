import csv
import pandas as pd
import os
import glob

def deg2time(deg):
    return 0.3/45 * deg

def time2deg(time):
    return 45/0.3 * time


def write2csv(path2file, Currents, Keys, Calib, Angles, Image_dir):
    with open(path2file + '_calib' + '.csv', 'w') as f:
        f.write("{}, {}, {}, {}, {}\n".format('Current', 'Key', 'Time', 'Angles', 'Image_dir'))
        try:
            for item in range(len(Currents)):
                f.write("{}, {}, {}, {}, {} \n".format(Currents[item], Keys[item], Calib[item], Angles[item], Image_dir[item]))
        except  IndexError:
             Image_dir.append(0)

def calibTime(path2file):
    with open(path2file  + '.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        Times = []
        Keys = []
        Calib = []
        Currents = []
        Angles = []

        for row in readCSV:
            Key = row[2]
            Time = row[1]
            Current = row[0]
            # Angle = row[3]

            Times.append(Time)
            Keys.append(Key)
            Currents.append(Current)

        for i in range(1, 2):
            Calib.append(float(Times[i]))
        for i in range(2, len(Times)):
            Calib.append(float(Times[i]) - float(Times[i-1]))
        # print(Calib)
        for i in range(0, len(Calib)):
            j = Keys[i]
            if j == " 'D'":
                value = time2deg(Calib[i])
                Angles.append(value)
                # print(Angles)
            elif j == " 'A'":
                # print(Calib[i])
                Angles.append(-1 * time2deg(Calib[i]))
            else:
                # print(Calib[i])
                Angles.append(0)

        # print(Calib)

    return Currents, Keys, Calib, Angles

def claibImage(path2img, path2file):
    img_dir = []
    jpgCounter = 0
    for file in glob.glob(path2img + "*.jpg"):
        img_dir.append(file)
    index = []
    Img_time = []
    Key_time = []
    Currents = []
    for root, dirs, files in os.walk('Data/IMG/'):
        for file in files:
            if file.endswith('.jpg'):
                img_dir.append(file)
                jpgCounter += 1
    # print(img_dir)
    for i in range(len(img_dir)):
        h = img_dir[i][1:3]
        m = img_dir[i][4:6]
        s = img_dir[i][7:9]
        append = [h, m, s]
        Img_time.append(append)
    # print(Img_time)


    with open(path2file  + '.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            Current = row[0]
            Currents.append(Current)

        for i in range(len(Currents)):
                h = Currents[i][1:3]
                m = Currents[i][4:6]
                s = Currents[i][7:9]
                append = [h, m, s]
                Key_time.append(append)
    # print(Key_time)
    clone = []


    # print(Img_time)
    print(Key_time[1])
    num = 0
    while not Img_time[num] == Key_time[1]:
        num += 1
    print(Img_time[num])
    print(num)
    counter = num
    for i in range((len(Key_time)+1)-len(Img_time)):
        Img_time.append(0)
    print(len(Key_time))
    print(len(Img_time))
    for i in range(1, len(Key_time)):
        # h =  Key_time[num + i][0]
        # m =  Key_time[num + i][1]
        # s =  Key_time[num + i][2]
        # h1 =  Img_time[counter][0]
        # m1 =  Img_time[counter][1]
        # s1 =  Img_time[counter][2]
        try:
            if Img_time[counter] == Key_time[i]:
                clone.append(img_dir[counter])
                print(img_dir[counter])
                # counter += 1
            else:
                counter += 1
        except  IndexError:
            img_dir.append(0)
    # print(img_dir)
    # print(clone)
    print(len(clone))
    print(len(Key_time))
    # print(img_dir)

    return clone

def claibImage2(path2img, path2file):
    img_dir = []
    for file in glob.glob(path2img + "*.jpg"):
        img_dir.append(file)

    return img_dir


#########################################################################################################
##                                      CONTROL FUNCTIONS                                              ##
##                                                                                                     ##
##                              Arduino_Serial.write(str.encode('l'))                                  ##
##                              Arduino_Serial.write(str.encode('r'))                                  ##
##                              Arduino_Serial.write(str.encode('f'))                                  ##
##                              Arduino_Serial.write(str.encode('b'))                                  ##
#########################################################################################################

import serial
import time


Arduino_Serial = serial.Serial('com5',9600)
print (Arduino_Serial.readline())


def forward():
    Arduino_Serial.write(str.encode('f'))

def backward():
    Arduino_Serial.write(str.encode('b'))

def left():
    Arduino_Serial.write(str.encode('l'))

def right():
    Arduino_Serial.write(str.encode('r'))


def stop():
    Arduino_Serial.write(str.encode('o'))

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
        Arduino_Serial.write(str.encode('l'))
        if countSec(duration):
            break
        else:
            continue

def right_ai(duration):
    while True:
        Arduino_Serial.write(str.encode('r'))
        if countSec(duration):
            break
        else:
            continue



def steer_angle(angle):
    duration = deg2time(angle)
    if angle < 0:
        while True:
            Arduino_Serial.write(str.encode('l'))
            if countSec(duration):
                break
            else:
                continue
    else:
        while True:
            Arduino_Serial.write(str.encode('r'))
            if countSec(duration):
                break
            else:
                continue



