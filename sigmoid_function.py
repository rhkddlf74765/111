import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-10,10,00.1)
def sigmoid_function(x):
    y= 1/(1+np.exp(-x))
    plt.title("sigmoid function")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.plot(x,y)
    print(y)
    plt.show()
sigmoid_function(x)