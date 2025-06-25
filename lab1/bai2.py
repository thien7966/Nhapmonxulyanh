import cv2
import numpy as np


img = cv2.imread(r'd:\download\VanLangUni\HK243\Nhap mon xu ly anh so\lab1\Exercise\baby.jpeg')


if img is None:
    print(" Không đọc được ảnh. Kiểm tra lại tên ảnh hoặc đường dẫn.")
    exit()


swapped = img[:, :, [2, 1, 0]] 


cv2.imwrite(r'd:\download\VanLangUni\HK243\Nhap mon xu ly anh so\lab1\Exercise\baby_swapped.jpg', swapped)

print(" Đã hoán đổi kênh màu và lưu ảnh thành công: baby_swapped.jpg")
