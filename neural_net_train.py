import tensorflow as tf
import numpy as np
import keras
from time import time
from tensorflow.python.keras.callbacks import TensorBoard
from sklearn.utils import class_weight
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
import matplotlib.pyplot as plt

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

NAME = "network_pid".format(int(time()))

X = np.load("nn_test.npy")
y = np.load("nn_result.npy")
control = np.load("nn_control.npy")
control_result = np.load("nn_control_result.npy")

y = np.array(y, ndmin=2).T
X = np.array(X, ndmin=2)


print(X)
print(y)

test_X = X

print(X)
print(y)

model = keras.Sequential([
    keras.layers.Dense(input_shape=(1,), units=2),
    keras.layers.Dense(32, activation=tf.nn.relu),
    keras.layers.Dense(16, activation=tf.nn.relu),
    keras.layers.Dense(8, activation=tf.nn.relu),
    keras.layers.Dense(1)
])

tensorboard = TensorBoard(log_dir='logs/{}'.format(NAME))

# sets optimization function, learning rate and loss function for network

#optimizer = tf.keras.optimizers.RMSprop(0.001)
#optimizer = keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
optimizer = tf.train.AdamOptimizer()
model.compile(loss='mean_squared_error',
            optimizer=optimizer,
            metrics=['mean_absolute_error', 'mean_squared_error'])

# trains the network for 1000 epochs with 500 iterations per epoch


# class PrintDot(keras.callbacks.Callback):
#
#     def on_epoch_end(self, epoch, logs):
#         if epoch % 100 == 0: print('')
#         print('.', end='')


EPOCHS = 10000

history = model.fit(
  X, y,
  epochs=EPOCHS,
  verbose=1,)

def variable_summaries(var):
    """Attach a lot of summaries to a Tensor (for TensorBoard visualization)."""
    with tf.name_scope('summaries'):
        mean = tf.reduce_mean(var)
        tf.summary.scalar('mean', mean)
        with tf.name_scope('stddev'):
            stddev = tf.sqrt(tf.reduce_mean(tf.square(var - mean)))
        tf.summary.scalar('stddev', stddev)
        tf.summary.scalar('max', tf.reduce_max(var))
        tf.summary.scalar('min', tf.reduce_min(var))
        tf.summary.histogram('histogram', var)
model.save('nn_model.h5')
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