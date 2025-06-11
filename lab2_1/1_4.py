from PIL import Image
import numpy as np
import matplotlib.pylab as plt


img = Image.open('world cup.jpg').convert('L')


iml = np.asarray(img)


bl = iml.flatten()


hist, bins = np.histogram(iml, 256, [0, 255])


cdf = hist.cumsum()


cdf_m = np.ma.masked_equal(cdf, 0)


num_cdf_m = (cdf_m - cdf_m.min()) * 255
den_cdf_m = cdf_m.max() - cdf_m.min()
cdf_m = num_cdf_m / den_cdf_m


cdf = np.ma.filled(cdf_m, 0).astype('uint8')


im2 = cdf[bl]


im3 = np.reshape(im2, iml.shape)


im4 = Image.fromarray(im3)


img.show()
im4.show()


plt.imshow(im4, cmap='gray')
plt.axis('off')
plt.title('Histogram Equalized Image')
plt.show()
