Lab 2_1
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Mở ảnh xám (grayscale)
img = Image.open('world_cup.jpg').convert('L')

# Chuyển ảnh thành mảng ndarray
im1 = np.asarray(img)

# Thực hiện phép biến đổi ảnh nghịch đảo (inversion)
im2 = 255 - im1

# Chuyển mảng ndarray trở lại ảnh
new_img = Image.fromarray(im2)

# Hiển thị ảnh gốc
img.show()

# Hiển thị ảnh mới bằng matplotlib
plt.imshow(new_img, cmap='gray')
plt.title('Inverted Image')
plt.axis('off')
plt.show()

Câu 2:
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Mở ảnh xám
img = Image.open('world cup.jpg').convert('L')

# Chuyển ảnh thành ndarray
im1 = np.asarray(img)

# Khởi tạo gamma
gamma = 0.5

# Chuyển kiểu dữ liệu từ int sang float
bl = im1.astype(float)

# Tìm giá trị lớn nhất trong ảnh
b2 = np.max(bl)

# Chuẩn hóa ảnh
b3 = bl / b2

# Áp dụng phép biến đổi gamma
b4 = np.log(b3 + 1e-8) * gamma  # Thêm giá trị nhỏ để tránh log(0)
c = np.exp(b4) * 255.0

# Chuyển về kiểu số nguyên 8-bit
cl = np.clip(c, 0, 255).astype(np.uint8)

# Tạo ảnh từ mảng
d = Image.fromarray(cl)

# Hiển thị ảnh gốc và ảnh sau khi gamma correction
img.show()
d.show()

# Hiển thị ảnh bằng matplotlib
plt.imshow(d, cmap='gray')
plt.title('Gamma Correction (γ = 0.5)')
plt.axis('off')
plt.show()

Câu 3:
from PIL import Image
import numpy as np
import matplotlib.pylab as plt

# mở một ảnh ở dạng xám (grayscale)
img = Image.open('world_cup.jpg').convert('L')

# chuyển ảnh thành mảng NumPy (ndarray)
im_1 = np.asarray(img)

# chuyển kiểu dữ liệu từ số nguyên sang số thực (float)
bl = im_1.astype(float)

# tìm giá trị lớn nhất trong mảng bl
b2 = np.max(bl)

# thực hiện biến đổi logarit trên ảnh
c = (128.0 * np.log(1 + bl)) / np.log(1 + b2)

# chuyển mảng c thành kiểu số nguyên (int)
cl = c.astype(int)

# tạo ảnh mới từ mảng dữ liệu đã xử lý
d = Image.fromarray(cl.astype(np.uint8))

# hiển thị ảnh gốc và ảnh sau biến đổi
img.show()
d.show()

# hiển thị ảnh bằng thư viện matplotlib
plt.imshow(d, cmap='gray')
plt.axis('off')
plt.show()


Câu 4:
from PIL import Image
import numpy as np
import matplotlib.pylab as plt

# mở một ảnh ở chế độ thang xám (grayscale)
img = Image.open('world cup.jpg').convert('L')

# chuyển ảnh thành một mảng NumPy (ndarray)
iml = np.asarray(img)

# chuyển mảng 2 chiều thành mảng 1 chiều (flatten)
bl = iml.flatten()

# tính histogram và các giá trị bin tương ứng
hist, bins = np.histogram(iml, 256, [0, 255])

# tính hàm phân phối tích lũy (CDF) của histogram
cdf = hist.cumsum()

# các vị trí có giá trị CDF = 0 sẽ bị che (mask), phần còn lại được lưu vào cdf_m
cdf_m = np.ma.masked_equal(cdf, 0)

# thực hiện cân bằng histogram (histogram equalization)
num_cdf_m = (cdf_m - cdf_m.min()) * 255
den_cdf_m = cdf_m.max() - cdf_m.min()
cdf_m = num_cdf_m / den_cdf_m

# các vị trí bị mask trong cdf_m được gán giá trị 0
cdf = np.ma.filled(cdf_m, 0).astype('uint8')

# áp dụng các giá trị CDF để ánh xạ lên mảng ảnh phẳng (1 chiều)
im2 = cdf[bl]

# im2 đang là mảng 1 chiều nên cần reshape thành ảnh 2 chiều ban đầu
im3 = np.reshape(im2, iml.shape)

# chuyển mảng im3 thành đối tượng ảnh
im4 = Image.fromarray(im3)

# hiển thị ảnh gốc và ảnh đã cân bằng histogram
img.show()
im4.show()

# hiển thị ảnh bằng thư viện matplotlib
plt.imshow(im4, cmap='gray')
plt.axis('off')
plt.title('Histogram Equalized Image')
plt.show()




Câu 5.
from PIL import Image
import math
import scipy
import numpy as np
import imageio.v2 as iio
import matplotlib.pylab as plt

# mở một ảnh ở chế độ thang xám (grayscale)
img = Image.open('world_cup.jpg').convert('L')

# chuyển ảnh thành mảng NumPy (ndarray)
iml = np.asarray(img)

# tìm giá trị pixel lớn nhất và nhỏ nhất trong ảnh
b = iml.max()
a = iml.min()
print(a, b)

# chuyển kiểu dữ liệu mảng iml thành float
C = iml.astype(float)

# thực hiện biến đổi tăng cường độ tương phản (contrast stretching)
im2 = 255 * (C - a) / (b - a)

# chuyển mảng im2 thành ảnh
im3 = Image.fromarray(im2.astype(np.uint8))

# hiển thị ảnh gốc và ảnh sau khi tăng cường độ tương phản
img.show()
im3.show()

# hiển thị ảnh bằng matplotlib
plt.imshow(im3, cmap='gray')
plt.axis('off')
plt.show()
Câu 6
from PIL import Image
import math
import scipy
import numpy as np
import imageio.v2 as iio
import matplotlib.pylab as plt

# mở một ảnh ở chế độ thang xám (grayscale)
img = Image.open('world cup.jpg').convert('L')

# chuyển ảnh thành mảng NumPy (ndarray)
iml = np.asarray(img)

# thực hiện biến đổi Fourier nhanh 2 chiều (FFT)
c = abs(scipy.fftpack.fft2(iml))

# dịch tâm ảnh phổ về trung tâm (shift FFT)
d = scipy.fftpack.fftshift(c)

# khởi tạo biến cho hàm tích chập
M = d.shape[0]
N = d.shape[1]

# khởi tạo bộ lọc H với tất cả giá trị bằng 1
H = np.ones((M, N))

center1 = M / 2
center2 = N / 2
d_0 = 30.0  # cut-off radius: bán kính cắt
t1 = 1      # the order of BLPF (Butterworth Lowpass Filter)
t2 = 2 * t1
# định nghĩa hàm lọc Butterworth thông thấp (BLPF)
for i in range(M):
    for j in range(N):
        rl = (i - center1) ** 2 + (j - center2) ** 2
        
        # tính khoảng cách Euclid từ tâm ảnh
        r = math.sqrt(rl)
        
        # sử dụng bán kính cắt để loại bỏ tần số cao
        if r > 0:
            H[i, j] = 1 / (1 + (r / d_0) ** t2)

# chuyển mảng H thành ảnh
H_img = Image.fromarray((H * 255).astype(np.uint8))

# performing the convolution
# thực hiện tích chập trong miền tần số
con = d * H

# tính độ lớn của ảnh sau khi biến đổi ngược FFT
e = abs(scipy.fftpack.ifft2(scipy.fftpack.ifftshift(con)))

# e is converted from ndarray to image
# chuyển kết quả thành ảnh để hiển thị
e = e.astype(float)
im3 = Image.fromarray(e.astype(np.uint8))

# hiển thị ảnh gốc và ảnh đã lọc Butterworth
img.show()
im3.show()

# hiển thị ảnh bằng matplotlib
plt.imshow(im3, cmap='gray')
plt.axis('off')
plt.title('Butterworth Lowpass Filtered Image')
plt.show()
