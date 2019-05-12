import urllib
import urllib.request
import cv2
import numpy as np
import time
from time import gmtime, strftime
from PIL import Image
import os

url = 'http://192.168.1.95:8080/shot.jpg'

if os.path.isdir("Data") and os.path.isdir("Data/IMG"):
    pass
else:
    os.mkdir('Data')
    os.mkdir('Data/IMG')
i = 0
while True:
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    im_pil = Image.fromarray(img)
    # all the opencv processing is done here
    im_pil.save("Data\\IMG\\{}_trainingImage_{}.jpg".format(strftime("$%H$%M$%S", gmtime()),i), 'JPEG')
    cv2.imshow('test',img)
    i+=1
    time.sleep(0.3)
    if ord('q')==cv2.waitKey(10):
        exit(0)