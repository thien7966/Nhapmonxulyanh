import cv2
import os
import numpy as np
import random


folder_path = r'd:\download\VanLangUni\HK243\Nhap mon xu ly anh so\lab1\Exercise'


for file in os.listdir(folder_path):
    if file.endswith('.jpg'):
        input_path = os.path.join(folder_path, file)

       
        img = cv2.imread(input_path)

        
        if img is None:
            print(f"❌ Không đọc được ảnh: {file}")
            continue

        
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        
        hue_shift = random.randint(30, 150)
        hsv[:, :, 0] = (hsv[:, :, 0] + hue_shift) % 180  

        
        new_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

       
        output_path = os.path.join(folder_path, f'random_hsv_{file}')
        cv2.imwrite(output_path, new_img)

        print(f"🌈 Đã tăng Hue {hue_shift}° cho {file} → random_hsv_{file}")
