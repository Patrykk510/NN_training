# Image processing
import cv2
import numpy as np
import os
import random

# Images directory
DATADIR = "Images"

# Categories of images
CATEGORIES = ["1", "2", "3", "4", "5"]

# Size of image
IMG_SIZE = 128

training_data = []

# Preparation of traing data
def create_training_data():
    for category in CATEGORIES:
        class_num = CATEGORIES.index(category)
        path = os.path.join(DATADIR, category)
        for img in os.listdir(path):
            img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
            img_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
            training_data.append([img_array, class_num])

create_training_data()

random.shuffle(training_data)

X = []
y = []

for features, label in training_data:
    X.append(features)
    y.append(label)

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

np.save('input_data', X)
np.save('output_data', y)