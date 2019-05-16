import pandas as pd  
data = pd.read_csv("Data/driving_log.csv",
       names = ['Img', 'Current', 'Time', 'Key',])

Imgs = data['Img']
Keys = data['Key']
Times = data['Time']
Current = data['Current']

for i in Imgs.count():
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

# print(Imgs.head())

  


