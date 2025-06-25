import cv2
import os
import numpy as np


folder_path = r'd:\download\VanLangUni\HK243\Nhap mon xu ly anh so\lab1\Exercise'


for file in os.listdir(folder_path):
    if file.endswith('.jpg'):
        input_path = os.path.join(folder_path, file)

        
        img = cv2.imread(input_path)

        
        if img is None:
            print(f" Không đọc được ảnh: {file}")
            continue

        
        rand_vals = np.random.randint(0, 256, 3)
        print(f"🎲 Thêm nhiễu RGB vào {file}: {rand_vals}")

        
        noisy_img = img.copy()
        for i in range(3):
            noisy_img[:, :, i] = np.clip(noisy_img[:, :, i] + rand_vals[i], 0, 255)

       
        output_path = os.path.join(folder_path, f'random_rgb_{file}')
        cv2.imwrite(output_path, noisy_img)
        print(f" Đã lưu ảnh nhiễu: random_rgb_{file}")
