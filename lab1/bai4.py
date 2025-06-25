import cv2
import numpy as np


img = cv2.imread(r'd:\download\VanLangUni\HK243\Nhap mon xu ly anh so\lab1\Exercise\baby.jpeg')
if img is None:
    print("Không thể đọc ảnh. Vui lòng kiểm tra lại đường dẫn.")
else:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(float)

   
    hsv[:, :, 0] = hsv[:, :, 0] / 3          
    hsv[:, :, 2] = hsv[:, :, 2] * 0.75       

    
    hsv = np.clip(hsv, 0, 255).astype(np.uint8)

    
    new_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    
    save_path = r'd:\download\VanLangUni\HK243\Nhap mon xu ly anh so\lab1\Exercise\baby_custom_hsv.jpeg'
    cv2.imwrite(save_path, new_img)
    
    print(f"Ảnh đã được xử lý và lưu tại: {save_path}")
