import pandas as pd  
data = pd.read_csv("Data/driving_log.csv", delimiter=',',
       names = ['Current', 'Time', 'Key',])

def deg2time(deg):
    return 0.3/45 * deg
def time2deg(time):
    return 45/0.3 * time
# Imgs = data['Img']
Keys = data['Key']
Times = data['Time']
Current = data['Current']
times = []

for index, content in data.Current:
    times.append(content)

print(times)
# for j in Keys:
#     i = 0
#     if j == 'd':
#         value = time2deg(Calib[i])
#         Angles.append(value)
#         # print(Angles)
#     elif j == 'a':
#         # print(Calib[i])
#         Angles.append(-1 * time2deg(Calib[i]))
#     else:
#         # print(Calib[i])
#         Angles.append(0)
#     i+=1
# print(Angles)
# print(Imgs.head())

  


