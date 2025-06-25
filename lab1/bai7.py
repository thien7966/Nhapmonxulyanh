import cv2
import os


folder_path = r'd:\download\VanLangUni\HK243\Nhap mon xu ly anh so\lab1\Exercise'


for file in os.listdir(folder_path):
    if file.endswith('.jpg'):
        input_path = os.path.join(folder_path, file)
        
       
        img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
        
        
        if img is None:
            print(f" Không đọc được ảnh: {file}")
            continue
        
        
        edges = cv2.Canny(img, 100, 200)
        
        
        output_path = os.path.join(folder_path, f'edges_{file}')
        
        
        cv2.imwrite(output_path, edges)
        print(f" Đã xử lý: {file} → edges_{file}")
