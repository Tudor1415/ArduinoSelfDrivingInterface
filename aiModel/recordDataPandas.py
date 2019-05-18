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
# times = [[i] for j, i in Current]
list(Current)
print(type(list(Current))



