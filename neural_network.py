import tensorflow as tf
import numpy as np
import keras
from time import time
from tensorflow.python.keras.callbacks import TensorBoard
from sklearn.utils import class_weight
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
import matplotlib.pyplot as plt
from keras.models import load_model


def learn(bac_array, user_input_array):
    X = bac_array
    y = user_input_array

    # creates model
    model = keras.Sequential([
        keras.layers.Dense(input_shape=(1,), units=2),
        keras.layers.Dense(32, activation=tf.nn.relu),
        keras.layers.Dense(16, activation=tf.nn.relu),
        keras.layers.Dense(8, activation=tf.nn.relu),
        keras.layers.Dense(1)
    ])

    # sets optimization function, learning rate and loss function for network
    optimizer = tf.train.AdamOptimizer()
    model.compile(loss='mean_squared_error',
                optimizer=optimizer,
                metrics=['mean_absolute_error', 'mean_squared_error'])


    EPOCHS = 10000

    # trains model
    history = model.fit(
      X, y,
      epochs=EPOCHS,
      verbose=1,)

    # saves model (duh)
    model.save('nn_model.h5')

    # predicts perceived drunkenness for any bac
def predict(bac):
    model = load_model('nn_model.h5')
    optimizer = tf.train.AdamOptimizer()
    model.compile(loss='mean_squared_error',
                  optimizer=optimizer,
                  metrics=['mean_absolute_error', 'mean_squared_error'])
    predictions = model.predict(bac)

    return predictions

