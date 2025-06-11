from PIL import Image
import numpy as np
import matplotlib.pylab as plt


img = Image.open('world_cup.jpg').convert('L')


im_1 = np.asarray(img)


bl = im_1.astype(float)


b2 = np.max(bl)


c = (128.0 * np.log(1 + bl)) / np.log(1 + b2)


cl = c.astype(int)


d = Image.fromarray(cl.astype(np.uint8))


img.show()
d.show()


plt.imshow(d, cmap='gray')
plt.axis('off')
plt.show()

