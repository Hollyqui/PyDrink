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

model = load_model('nn_model.h5')
optimizer = tf.train.AdamOptimizer()
model.compile(loss='mean_squared_error',
            optimizer=optimizer,
            metrics=['mean_absolute_error', 'mean_squared_error'])

control = np.load("nn_control.npy")
control_result = np.load("nn_control_result.npy")

predictions = model.predict(control)

print(control)
print(predictions)
print(control_result)

plt.plot(control, predictions)
plt.show()

plt.plot(control, control_result)
plt.show()
np.save("np_predictions", predictions)
np.save("np_y", y)