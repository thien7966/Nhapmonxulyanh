from PIL import Image
import math
import scipy
import numpy as np
import imageio.v2 as iio
import matplotlib.pylab as plt

img = Image.open('world_cup.jpg').convert ('L')

iml = np.asarray(img)

b = iml.max ()
a = iml.min()
print (a, b)

C = iml.astype (float)

im2 = 255* (c- a)/(b -a)

im3 = Image.fromarray (im2)
img.show ()
im3.show ()
plt.imshow(im3)
plt.show ()