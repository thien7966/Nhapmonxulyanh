from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


img = Image.open('world cup.jpg').convert('L')


im1 = np.asarray(img)


gamma = 0.5


bl = im1.astype(float)


b2 = np.max(bl)


b3 = bl / b2


b4 = np.log(b3 + 1e-8) * gamma  
c = np.exp(b4) * 255.0


cl = np.clip(c, 0, 255).astype(np.uint8)


d = Image.fromarray(cl)


img.show()
d.show()


plt.imshow(d, cmap='gray')
plt.title('Gamma Correction (γ = 0.5)')
plt.axis('off')
plt.show()
