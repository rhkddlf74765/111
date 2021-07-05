import numpy as np
import matplotlib.pyplot as plt
def softmax_function(x):
    tmp=np.max(x)  
    y=np.exp(x-tmp)/np.sum(np.exp(x-tmp))
    plt.title("softmax function")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.plot(x,y)
    print(y)
    plt.show()
x=np.arange(-15,40)
print(softmax_function(x))