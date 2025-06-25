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
        
        
        median = cv2.medianBlur(img, 5)
        gaussian = cv2.GaussianBlur(img, (5, 5), 0)
        bilateral = cv2.bilateralFilter(img, 9, 75, 75)

        # Lưu ảnh với tiền tố tương ứng
        cv2.imwrite(os.path.join(folder, f'median_{file}'), median)
        cv2.imwrite(os.path.join(folder, f'gaussian_{file}'), gaussian)
        cv2.imwrite(os.path.join(folder, f'bilateral_{file}'), bilateral)
        
        print(f"Đã xử lý và lưu: median_{file}, gaussian_{file}, bilateral_{file}")
