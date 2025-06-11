from PIL import Image
import math
import scipy
import numpy as np
import imageio.v2 as iio
import matplotlib.pylab as plt

img = Image.open('world cup.jpg').convert('L')

iml = np.asarray(img)

c= abs (scipy.fftpack.fft2(iml))

d = scipy.fftpack.fftshift(c)

M = d.shape [0]
N = d.shape[l]

H= np.ones((M, N))
centerl = M/2
center2 = N/2
d_0 =30.0 
t1 = 1 
t2 = 2 * tl

for i in range (1, M):
    for j in range (1, N) :
        rl = (i- centerl) **2 + (j - center2) **2

        r = math.sqrt (rl)

        if r > d_0:
            H [i, 3] = 1/(1 + (r/d_0) **t2)

H= H.astype (float)
H = Image.fromarray(H)

con =d*H

e = abs (scipy.fftpack.ifft2(con))

e = e.astype (float)
im3 = Image.fromarray (e)
img.show ()
im3.show ()
plt.imshow(im3)
plt.show ()