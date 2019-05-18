import pandas as pd
data = pd.read_csv("Data/driving_log.csv", delimiter=',',
       names = ['Img', 'Current', 'Time', 'Key', 'Calibrated_Time', 'Angles'])

def deg2time(deg):
    return 1/45 * deg
def time2deg(time):
    return 45/1 * time
# Imgs = data['Img']
Keys = data['Key']
Times = data['Time']
Current = data['Current']
times = []
calib = []
angles = []
keys = []
# times = [[i] for j, i in Current]
# print(data['Current'])

# print(type(list(Current))
for i, row in data.iterrows():
    times.append(row['Time'])
    keys.append(row['Key'])
# print(keys)
calib.append(times[0])
for i in range(1, len(times)):
    calib.append(float(times[i]) - float(times[i-1]))
# print(calib)

for i in range(0, len(calib)):
    j = keys[i]
    if j == " 'a'":
        value = time2deg(calib[i])
        angles.append(value)
        # print(Angles)
    elif j == " 'd'":
        # print(Calib[i])
        angles.append(-1 * time2deg(calib[i]))
    else:
        # print(Calib[i])
        angles.append(0)
# print(angles)

# df=pd.DataFrame({'Calibrated_Time':calib})
# df2=pd.DataFrame({'Angles':angles})
# df2.append(df)
# data.append(df2)
# print(df)
data['Calibrated_Time'] = calib
data['Angles'] = angles
print(data)
data.to_csv (r'Data\driving_log_calib.csv', index = None, header=True)