import csv
import pandas as pd

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
        for row in readCSV:
            Key = row[2]
            Time = row[1]
            Current = row[0]

            Times.append(Time)
            Keys.append(Key)
            Currents.append(Current)

        print(len(Keys))
        print(len(Currents))
        for i in range(0, 2):
            Calib.append(Times[i])
        for i in range(2, len(Times)):
            Calib.append(float(Times[i]) - float(Times[i-1]))
        print(len(Calib))
    with open(path2file + '_calib' + '.csv', 'w') as f:
        f.write("{}, {}, {}\n".format('Current', 'Time', 'Key'))
        for item in range(len(Currents)):
            f.write("{}, {}, {}\n".format(Currents[item], Keys[item], Calib[item]))
    return Calib

