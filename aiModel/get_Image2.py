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

def get_image(url, choice, i):
    if choice == True:
        size = 128, 128
        imgResp=urllib.request.urlopen(url)
        imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
        img=cv2.imdecode(imgNp,-1)
        im_pil = Image.fromarray(img)
        im_pil.save("Data\\IMG\\{}_trainingImage_{}.jpg".format(strftime("$%H$%M$%S", gmtime()), i), 'JPEG')
        return 'Data\\IMG\\{}_trainingImage_{}.jpg'.format(strftime("$%H$%M$%S", gmtime()),i )
    elif choice == False:
        return None
