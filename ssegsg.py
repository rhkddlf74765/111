import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
img=Image.open("practice1.png")
# plt.imshow(img)
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("picture")
# plt.legend(loc=(1,1),fontsize=14,frameon=True, shadow=False)
# plt.show()
img.show()
im=np.array(img)
print(im)

