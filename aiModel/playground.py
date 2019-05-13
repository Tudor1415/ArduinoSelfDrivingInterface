# img_dir = "$12$36$28"
# index = []
# for pos, char in enumerate(img_dir):
#     if char == '$':
#         index.append(pos)
#         print(index)

# h = img_dir[index[0]+1:index[0]+3]
# m = img_dir[index[1]+1:index[1]+3]
# s = img_dir[index[2]+1:index[2]+3]





# print("The time is {}, {}, {}".format(h, m, s))
# list = [" 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'"," 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", "'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'", " 'D'", " 'W'" ]

# for i in list:
#     # print(i)
#     if i == " 'W'":
#         print('forward')
#     if i == " 'D'":
#         print('right')




# def time2deg(time):
#     return 45/1 * time

# print(time2deg(0.3))

import datetime

# currentDT = datetime.datetime.now()

# print ("Current Year is: %d" % currentDT.year)
# print ("Current Month is: %d" % currentDT.month)
# print ("Current Day is: %d" % currentDT.day)
# print ("Current Hour is: %d" % currentDT.hour)
# print ("Current Minute is: %d" % currentDT.minute)
# print ("Current Second is: %d" % currentDT.second)
# print ("Current Microsecond is: %d" % currentDT.microsecond)

currentDT = datetime.datetime.now()
print (str(currentDT))