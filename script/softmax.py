import numpy as np
import sys, os
import pickle
import matplotlib.pyplot as plt
sys.path.append(os.pardir)
print("os:pardir", os.pardir)
from PIL import Image
from dataset.mnist import load_mnist


def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(
        normalize=True, flatten=True, one_hot_label=False
    )
    return x_test, t_test


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


def init_network():
    with open("sample_weight.pkl", "rb") as f:
        network = pickle.load(f)

    return network


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


def sigmoid(x):
    return 1 /(1 + np.exp(-x))


def predict(network, x):
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y=softmax(a3)
    return y

def cross_entropy_error(y,t):
  delta = 1e-7
  return -np.sum(t*np.log(y+delta))

def test_cross_entropy_error():
  t = [1]
  y=[0.1]
  ans=cross_entropy_error(np.array(y),np.array(t))
  print("crorrs;",ans)

def check():
    x, t = get_data()
    network = init_network()
    accuracy_cnt = 0
    for i in range(len(x)):
        y = predict(network, x[i])
        p = np.argmax(y)

        if p == t[i]:
            accuracy_cnt += 1
    print("Accuracy:" + str(float(accuracy_cnt) / len(x)))

def test_batch_train():
  x,t=get_data()
  train_size= x.shape[0]
  print("train_size:",x)
  batch_size =10
  batch_mask=np.random.choice(train_size,batch_size)
  x_batch = x[batch_mask]
  t_batch=  t[batch_mask]
  print("x_batch:",x_batch)

def function_1(x):
  return 0.01*x**2 + 0.1*x


def draw_function_1():
  x = np.arange(0.0,20.0,0.1)
  y=function_1(x)
  plt.xlabel("x")
  plt.ylabel("f(x)")
  plt.plot(x,y)

  plt.show(block=True)


draw_function_1()

