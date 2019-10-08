# coding: utf-8
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('env', 'KERAS_BACKEND=tensorflow')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

print("ok")
from keras.datasets import mnist

from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train/255
x_test = x_test/255
from keras.utils import np_utils
y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)
y_train[9]
from keras.models import Sequential

# 矩陣拉平
from keras.layers import Dense, Flatten

# 抽樣的時候不按照順序
from keras.optimizers import SGD
model = Sequential()
model.add(Flatten(input_shape=(28, 28)))
model.add(Dense(6, activation="relu"))
model.add(Dense(5, activation="relu"))
model.add(Dense(4, activation="relu"))
# 結果輸出層
model.add(Dense(10, activation="softmax"))
model.compile(loss='mse', optimizer=SGD(lr=0.087), metrics=['accuracy'])
model.summary()
# 4710 para
# 784 連到 6 個神經元 加六個 bias
784*6 + 6

# batch_size 幾筆資料就調參數對答案
# 全部資料要學幾次

model.fit(x_train, y_train, batch_size=100, epochs=20)
model = Sequential()
model.add(Flatten(input_shape=(28, 28)))
model.add(Dense(6, activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(4, activation="relu"))
# 結果輸出層
model.add(Dense(10, activation="softmax"))
model.compile(loss='mse', optimizer=SGD(lr=0.57), metrics=['accuracy'])
model.summary()
# 4710 para
# 784 連到 6 個神經元 加六個 bias
784*6 + 6

# batch_size 幾筆資料就調參數對答案
# 全部資料要學幾次

model.fit(x_train, y_train, batch_size=80, epochs=25)
model = Sequential()
model.add(Flatten(input_shape=(28, 28)))
model.add(Dense(10, activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(5, activation="relu"))
# 結果輸出層
model.add(Dense(10, activation="softmax"))
model.compile(loss='mse', optimizer=SGD(lr=0.77), metrics=['accuracy'])
model.summary()
# 4710 para
# 784 連到 6 個神經元 加六個 bias
784*6 + 6

# batch_size 幾筆資料就調參數對答案
# 全部資料要學幾次

model.fit(x_train, y_train, batch_size=70, epochs=25)
from ipywidgets import interact_manual
predict = model.predict(x_test)
predict[1234]
predict = model.predict_classes(x_test)
predict[1234]
y_test[1234]
def test(no):
    plt.imshow(x_test[no], cmap="Blues")
    print("We predict", predict[no])
test(123)
interact_manual(test, no=(0, 9999))
score = model.evaluate(x_test, y_test)
score[1]
model_json = model.to_json()
open('smart_model.json', 'w').write(model_json)
model.save_weights('smart_model_weights.h5')
