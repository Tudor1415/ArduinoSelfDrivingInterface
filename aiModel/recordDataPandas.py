import pandas as pd  
from helpers import *
data = pd.read_csv("Data/driving_log.csv",
       names = ['Current', 'Time', 'Key',])

# Imgs = data['Img']
Keys = data['Key']
Times = data['Time']
Current = data['Current']
Angles = []
for j in Keys:
    if j == 'd':
        value = time2deg(Calib[i])
        Angles.append(value)
        # print(Angles)
    elif j == 'a':
        # print(Calib[i])
        Angles.append(-1 * time2deg(Calib[i]))
    else:
        # print(Calib[i])
        Angles.append(0)
print(Angles)
# print(Imgs.head())

  


