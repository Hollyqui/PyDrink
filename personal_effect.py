import tensorflow as tf
import numpy as np
from tensorflow import keras
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
# X = tf.keras.utils.normalize(
#         X,
#         axis=-1,
#         order=2
#         )

print(X)
print(y)

model = keras.Sequential([
    keras.layers.Dense(input_shape=(1,), units=2),
    keras.layers.Dense(32, activation=tf.nn.leaky_relu),
    keras.layers.Dense(16, activation=tf.nn.leaky_relu),
    keras.layers.Dense(8, activation=tf.nn.leaky_relu),
    keras.layers.Dense(1)
])

tensorboard = TensorBoard(log_dir='logs/{}'.format(NAME))

# sets optimization function, learning rate and loss function for network

optimizer = tf.keras.optimizers.RMSprop(0.001)
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


EPOCHS = 1000

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




predictions = model.predict(control)


# k= 0
# prediction = []
# for i in predictions:
#    prediction.append(int(np.argmax(predictions[k])))
#    real_result = y[k][0]
#    k = k + 1
# prediction=np.array(prediction, ndmin=2).T
print(control)
print(predictions)
print(control_result)

# for i in range(3):
#     stored_labels = y.T[0]
#     temp_labels = []
#     temp_predictions = predictions.T[i] #(iterates through the columns)
#     for j in range(len(y)):
#         if stored_labels[j] == i:
#             temp_labels.append(1)
#         else:
#             temp_labels.append(0)
#     fpr_keras0, tpr_keras0, thresholds_keras0 = roc_curve(temp_labels, temp_predictions)
#     auc_keras0 = auc(fpr_keras0, tpr_keras0)
#     plt.figure(1)
#     plt.plot([0, 1], [0, 1], 'k--')
#     plt.plot(fpr_keras0, tpr_keras0, label='Keras0 (area = {:.3f})'.format(auc_keras0))



# plt.xlabel('False positive rate')
# plt.ylabel('True positive rate')
# plt.title('ROC curve')
# plt.legend(loc='best')
# plt.show()
# with tf.Session():
#     print('Confusion Matrix: \n\n', tf.Tensor.eval(confusion_matrix,feed_dict=None, session=None))

plt.plot(control, predictions)
plt.show()

plt.plot(control, control_result)
plt.show()
np.save("np_predictions", predictions)
np.save("np_y", y)