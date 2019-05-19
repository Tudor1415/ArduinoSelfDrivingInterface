import numpy as np
from PIL import Image
from io import BytesIO
import urllib
import cv2
from helpers import *
#load our saved model
from keras.models import load_model
from utils import *
from helpers import *
import time
url = 'http://192.168.1.95:8080/shot.jpg'
model = load_model('Model/model.h5')

MAX_SPEED = 7
MIN_SPEED = 2

while True:
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    image = utils.preprocess(ImgNp)
    steering_angle = float(model.predict(image, batch_size=1))
    steer_angle(steering_angle)
    forward()
    time.sleep(0.2)
    stop()
    steer_angle(steering_angle)
    time.sleep(0.4)


    print('{}'.format(steering_angle))
    if ord('q')==cv2.waitKey(10):
        exit(0)
