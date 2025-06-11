from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


img = Image.open('world_cup.jpg').convert('L')


im1 = np.asarray(img)


im2 = 255 - im1


new_img = Image.fromarray(im2)


img.show()


plt.imshow(new_img, cmap='gray')
plt.title('Inverted Image')
plt.axis('off')
plt.show()

