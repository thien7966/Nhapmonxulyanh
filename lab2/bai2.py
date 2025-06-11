import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# Đường dẫn thư mục
input_folder = r"D:\download\VanLangUni\HK243\Nhap mon xu ly anh so\lab2\exercise"
output_folder = r"D:\download\VanLangUni\HK243\Nhap mon xu ly anh so\lab2\bai2"
os.makedirs(output_folder, exist_ok=True)

# Hàm FFT
def fast_fourier_transform(img):
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    magnitude = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]) + 1)
    return np.uint8(cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX))

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

# Chương trình chính
def main():
    print("Chọn phương pháp biến đổi ảnh:\n[F]ast Fourier\n[L]owpass Butterworth\n[H]ighpass Butterworth")
    key = input("Nhập F, L hoặc H: ").upper()

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            img_path = os.path.join(input_folder, filename)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

            if key == 'F':
                result = fast_fourier_transform(img)
                output_name = f"{os.path.splitext(filename)[0]}_fft.png"
            elif key == 'L':
                result = apply_butterworth_filter(img, highpass=False)
                output_name = f"{os.path.splitext(filename)[0]}_bw_low.png"
            elif key == 'H':
                result = apply_butterworth_filter(img, highpass=True)
                output_name = f"{os.path.splitext(filename)[0]}_bw_high.png"
            else:
                print("Phím không hợp lệ. Thoát chương trình.")
                return

            out_path = os.path.join(output_folder, output_name)
            cv2.imwrite(out_path, result)
            print(f"Đã lưu ảnh: {out_path}")

if __name__ == "__main__":
    main()
