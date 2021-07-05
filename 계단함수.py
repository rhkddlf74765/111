import numpy as np
import matplotlib.pyplot as plt
def step_fuction(x):
    y= np.array(x>0,dtype=np.int)
    plt.plot(x,y)
    plt.title("step function")
    plt.axis([-5,5,-0.1,1.1])
    print(y)
    plt.show()

x=np.arange(-5,5,0.1)
step_fuction(x)

