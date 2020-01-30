import numpy as np
import os, io
import sys
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import paramiko as ssh

input_data = np.load('input_data.npy')
output_data = np.load('output_data.npy')

def slave_train(ip, password, name):
    # Neural network model
    model = Sequential()
    # Convolution layer
    model.add(Conv2D(128, (3, 3), input_shape=input_data.shape[1:]))
    model.add(Activation("relu"))
    # Pooling layer
    model.add(MaxPooling2D(pool_size=(2, 2)))
    # Convolution layer
    model.add(Conv2D(128, (3, 3)))
    model.add(Activation("relu"))
    # Pooling layer
    model.add(MaxPooling2D(pool_size=(2, 2)))
    # Dense layer
    model.add(Flatten())
    model.add(Dense(128))
    model.add(Activation("relu"))
    # Output layer
    model.add(Dense(5))
    model.add(Activation("softmax"))

    model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

    host_name=ip
    host_password=password
    slave=ssh.SSHClient()
    slave.set_missing_host_key_policy(ssh.AutoAddPolicy)
    slave.connect(host_name, port=2222, username="root", password=host_password)
    slave_sftp=slave.open_sftp()
    knn.save('model_{0}.h5'.format(name))
    slave_sftp.put('model_{0}.h5'.format(name), '/model.h5')
    model_trained=None
    slave.exec_command("python /slavescript.py")
    slave_sftp.get('/model_trained.h5', 'model_trained_{0}.h5'.format(name))
    slave_sftp.remove('/model_trained.h5')
    slave.close()

slave_train(sys.argv[1], sys.argv[2], '1')
slave_train(sys.argv[3], sys.argv[4], '2')