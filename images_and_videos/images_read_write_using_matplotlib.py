import matplotlib.pyplot as plt
import matplotlib.image as image
import numpy as np

# reading an image to a numpy array
img = image.imread("download.jpeg")
print(img.shape)
plt.imshow(img)
plt.show()

# saving a numpy array as image
plt.imsave("hello.jpeg", img)
