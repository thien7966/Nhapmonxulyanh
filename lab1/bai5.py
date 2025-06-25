import os
import cv2

folder = r'd:\download\VanLangUni\HK243\Nhap mon xu ly anh so\lab1\Exercise'

for file in os.listdir(folder):
    if file.lower().endswith('.jpg'):
        img_path = os.path.join(folder, file)
        img = cv2.imread(img_path)
        
        if img is None:
            print(f"Không thể đọc ảnh: {img_path}")
            continue
        
      
        blurred = cv2.blur(img, (5, 5))
        
        
        save_path = os.path.join(folder, f'mean_{file}')
        cv2.imwrite(save_path, blurred)
        
        print(f"Đã xử lý và lưu: {save_path}")
