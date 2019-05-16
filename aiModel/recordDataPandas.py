import pandas as pd  
data = pd.read_csv("filename.csv", delimeter = ',',
       names = ['Img', 'Current', 'Time', 'Key' ])

Imgs = data['Img']
Keys = data['Key']
Times = data['Time']
Current = data['Current']

for i in range(0, len(Imgs)):
  


