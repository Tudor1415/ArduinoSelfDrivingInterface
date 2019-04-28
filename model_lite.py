import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.contrib import lite

model = keras.Sequential([keras.layers.Dense(units= 1, input_shape = [1])])
model.compile(optimizer = 'sgd', loss='mean_squared_error')

def generate_data(ni):
    data_x = np.array()
    data_y = np.array()
    for i in range(ni):
        np.insert(data_y, [i*2-1])
        np.insert(data_x, i)
    return data_x, data_y

data_x, data_y = generate_data(100)

print(data_y)

