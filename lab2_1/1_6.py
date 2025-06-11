from PIL import Image
import math
import scipy
import numpy as np
import imageio.v2 as iio
import matplotlib.pylab as plt

img = Image.open('world cup.jpg').convert('L')

iml = np.asarray (img)

c= abs (scipy.fftpack.fft2 (iml))

d= scipy.fftpack.fftshift (c)
d = d.astype (float)

im3 = Image.fromarray (d)
img.show ()
im3.show()
plt.imshow (im3)
plt.show ()
