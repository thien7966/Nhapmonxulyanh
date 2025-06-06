import cv2
import numpy as np
import os
import random

# Đường dẫn
input_folder = r"D:\download\VanLangUni\HK243\Nhap mon xu ly anh so\lab2\exercise"
output_folder = r"D:\download\VanLangUni\HK243\Nhap mon xu ly anh so\lab2\bai3"
os.makedirs(output_folder, exist_ok=True)

# Các phép biến đổi ảnh từ bài 1
def inverse(img):
    return 255 - img

def gamma_correction(img, gamma=2.2):
    return np.uint8(255 * ((img / 255.0) ** (1 / gamma)))

def log_transform(img):
    c = 255 / np.log(1 + np.max(img))
    return np.uint8(c * np.log(1 + img))

def histogram_equalization(img):
    return cv2.equalizeHist(img)

def contrast_stretch(img):
    min_val = np.min(img)
    max_val = np.max(img)
    if max_val - min_val == 0:
        return img
    return np.uint8((img - min_val) * 255 / (max_val - min_val))

# Chọn hàm biến đổi ngẫu nhiên
def apply_random_transform(channel):
    transforms = [
        inverse,
        gamma_correction,
        log_transform,
        histogram_equalization,
        contrast_stretch
    ]
    transform = random.choice(transforms)
    return transform(channel)

# Chương trình chính
def main():
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            img_path = os.path.join(input_folder, filename)
            img = cv2.imread(img_path)

            # Đảo thứ tự kênh màu RGB
            channels = cv2.split(img)
            transformed_channels = [apply_random_transform(ch) for ch in channels]
            result = cv2.merge(transformed_channels[::-1])  # Đảo thứ tự RGB

            # Lưu ảnh
            output_name = f"{os.path.splitext(filename)[0]}_rgb_random.png"
            output_path = os.path.join(output_folder, output_name)
            cv2.imwrite(output_path, result)
            print(f"Đã xử lý và lưu: {output_path}")

if __name__ == "__main__":
    main()
