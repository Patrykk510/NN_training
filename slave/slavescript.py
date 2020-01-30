import numpy as np
import os
import sys
import random
import keras

input_data = np.load('input_data.npy')
output_data = np.load('output_data.npy')

model=keras.models.load_model('/model.h5')
os.remove('/model.h5')

model.fit(input_data, output_data, batch_size=4, epochs=10, validation_split=0.2)
model.save('/model_trained.h5')