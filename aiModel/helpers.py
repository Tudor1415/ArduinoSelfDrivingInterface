import csv
import pandas as pd
import os

def deg2time(deg):
    return 1/45 * deg

def time2deg(time):
    return 45/1 * time


def write2csv(path2file, text):

    csv.register_dialect('myDialect',
    delimiter = '|',
    quoting=csv.QUOTE_NONE,
    skipinitialspace=True)

    with open(path2file, 'w') as f:
        writer = csv.writer(f, dialect='myDialect')
        for row in text:
            writer.writerow(row)
    print('Finished')
    f.close()

def calibTime(path2file):
    with open(path2file  + '.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        Times = []
        Keys = []
        Calib = []
        Currents = []
        Angles = []
        Image_dir = []
        jpgCounter = 0

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

        print(len(Angles))
        print(Keys)
        print(len(Currents))
        print(len(Calib))
        print(len(Image_dir))
        # print(Calib)
    with open(path2file + '_calib' + '.csv', 'w') as f:
        f.write("{}, {}, {}, {}, {}\n".format('Current', 'Key', 'Time', 'Angles', 'Image_dir'))
        for item in range(len(Currents)):
            f.write("{}, {}, {}, {}, {} \n".format(Currents[item], Keys[item], Calib[item], Angles[item], Image_dir[item]))
    return Calib

def claibImage(path2img, path2file):
    img_dir = []
    for file in glob.glob(path2img + "*.jpg"):
        img_dir.append(file)
    index = []
    Img_time = []
    Key_time = []
    Currents = []
    for i in range(len(img_dir)):
        for pos, char in enumerate(img_dir):
            if char == '$':
                index.append(pos)
                # print(index)

        h = img_dir[index[0]+1:index[0]+3]
        m = img_dir[index[1]+1:index[1]+3]
        s = img_dir[index[2]+1:index[2]+3]
        Img_time.append('{} {} {}'.format(h, m, s))

    for root, dirs, files in os.walk('Data/IMG/'):
        for file in files:
            if file.endswith('.jpg'):
                jpgCounter += 1
                Image_dir.append('{}_Data/IMG/trainingImage_{}.jpg'.format(Img_time[jpgCounter], jpgCounter))
    with open(path2file  + '.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            Current = row[0]
            Currents.append(Current)

        for i in range(len(Currents)):
            for pos, char in enumerate(Currents):
                if char == '$':
                    index.append(pos)
                    # print(index)

            h = img_dir[index[0]+1:index[0]+3]
            m = img_dir[index[1]+1:index[1]+3]
            s = img_dir[index[2]+1:index[2]+3]
            append = [h, m, s]
            Key_time.append(append)
    
    # for i in range(len(Key_time)):
    #     h =  Key_time[i][0]
    #     m =  Key_time[i][1]
    #     s =  Key_time[i][2]

    

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



