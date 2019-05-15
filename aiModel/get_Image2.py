import urllib
import urllib.request
import cv2
import numpy as np
import time
from time import gmtime, strftime
from PIL import Image
import os

# url = 'http://192.168.1.95:8080/shot.jpg'

# if os.path.isdir("Data") and os.path.isdir("Data/IMG"):
#     pass
# else:
#     os.mkdir('Data')
#     os.mkdir('Data/IMG')

def get_image(url, choice):
    if choice == True:
        size = 128, 128
        imgResp=urllib.request.urlopen(url)
        imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
        img=cv2.imdecode(imgNp,-1)
        im_pil = Image.fromarray(img)
        # all the opencv processing is done here
        f = open('Data/driving_log.csv', 'r+')
        buffer = f.read()
        f.close()

        # im_pil.thumbnail(size, Image.ANTIALIAS)
        im_pil.save("Data\\IMG\\{}_trainingImage.jpg".format(strftime("$%H$%M$%S", gmtime())), 'JPEG')

        length = len(open("Data/driving_log.csv").readlines())
        f = open('Data/driving_log.csv', 'w')
        buffer += "'Data\\IMG\\{}_trainingImage.jpg, '".format(strftime("$%H$%M$%S", gmtime()))
        f.write(buffer)
    else:
        f = open('Data/driving_log.csv', 'r+')
        buffer = f.read()
        f.close()
        f = open('Data/driving_log.csv', 'w')
        buffer += "None, "
        f.write(buffer)
    # cv2.imshow('test',img)

    # time.sleep(0.2)
    # if ord('q')==cv2.waitKey(10):
    #     exit(0)