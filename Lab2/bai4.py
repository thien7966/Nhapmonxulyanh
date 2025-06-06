import cv2
import numpy as np
import os
import random

# Đường dẫn
input_folder = r"D:\download\VanLangUni\HK243\Nhap mon xu ly anh so\lab2\exercise"
output_folder = r"D:\download\VanLangUni\HK243\Nhap mon xu ly anh so\lab2\bai4"
os.makedirs(output_folder, exist_ok=True)

# Hàm tạo bộ lọc Butterworth
def butterworth_filter(shape, cutoff, order, highpass=False):
    rows, cols = shape
    u = np.arange(rows)
    v = np.arange(cols)
    u, v = np.meshgrid(u - rows // 2, v - cols // 2, indexing='ij')
    d = np.sqrt(u**2 + v**2)
    if highpass:
        h = 1 / (1 + (cutoff / (d + 1e-5)) ** (2 * order))
    else:
        h = 1 / (1 + (d / cutoff) ** (2 * order))
    return h

# Áp dụng Butterworth
def apply_butterworth_filter(img, cutoff=30, order=2, highpass=False):
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    h = butterworth_filter(img.shape, cutoff, order, highpass)
    h = np.repeat(h[:, :, np.newaxis], 2, axis=2)
    filtered = dft_shift * h
    f_ishift = np.fft.ifftshift(filtered)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
    return np.uint8(cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX))

# Min/Max Filter
def min_filter(img):
    return cv2.erode(img, np.ones((3, 3), np.uint8))

def max_filter(img):
    return cv2.dilate(img, np.ones((3, 3), np.uint8))


def main():
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            img_path = os.path.join(input_folder, filename)
            img = cv2.imread(img_path)

            
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            b, g, r = cv2.split(img_rgb)
            shuffled = [b, g, r]
            random.shuffle(shuffled)
            img_shuffled = cv2.merge(shuffled)

           
            img_gray = cv2.cvtColor(img_shuffled, cv2.COLOR_RGB2GRAY)

           
            highpass = random.choice([True, False])
            result = apply_butterworth_filter(img_gray, highpass=highpass)

            
            if highpass:
                result = max_filter(result)
                suffix = "_highpass_max"
            else:
                result = min_filter(result)
                suffix = "_lowpass_min"

            
            output_name = f"{os.path.splitext(filename)[0]}{suffix}.png"
            output_path = os.path.join(output_folder, output_name)
            cv2.imwrite(output_path, result)
            print(f"Đã xử lý và lưu: {output_path}")

if __name__ == "__main__":
    main()
