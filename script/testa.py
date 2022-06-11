import numpy as np
import sys, os
import pickle
import matplotlib.pyplot as plt
sys.path.append(os.pardir)

from dataset.mnist import load_mnist
print("os:pardir", os.pardir)
from PIL import Image




def function_1(x):
  return 0.01*x**2 + 0.1*x


def draw_function_1():
  x = np.arange(0.0,20.0,0.1)
  y=function_1(x)
  plt.xlabel("x")
  plt.ylabel("f(x)")
  plt.plot(x,y)

  plt.show()


draw_function_1()

