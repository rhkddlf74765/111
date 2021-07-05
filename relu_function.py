import numpy as np
import matplotlib.pyplot as plt
def relu_function(x):
    y=np.maximum(0,x)
    plt.title("relu function")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.plot(x,y)
    print(y)
    plt.show()
x=np.arange(-5,5)
relu_function(x)