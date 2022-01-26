import numpy as np
from matplotlib import pyplot as plt


def f(x):
   return x*x-4*x+4

x = np.linspace(-2, 6,20)

plt.plot(x, f(x),'.', color='red',linewidth="3")

plt.show()
