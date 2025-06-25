import cv2
import numpy as np


img = cv2.imread(r'd:\download\VanLangUni\HK243\Nhap mon xu ly anh so\lab1\Exercise\baby.jpeg')


if img is None:
    print("Không đọc được ảnh. Kiểm tra lại đường dẫn hoặc tên ảnh.")
    exit()


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


h, s, v = cv2.split(hsv)


cv2.imwrite(r'd:\download\VanLangUni\HK243\Nhap mon xu ly anh so\lab1\Exercise\baby_hue.jpg', h)
cv2.imwrite(r'd:\download\VanLangUni\HK243\Nhap mon xu ly anh so\lab1\Exercise\baby_saturation.jpg', s)
cv2.imwrite(r'd:\download\VanLangUni\HK243\Nhap mon xu ly anh so\lab1\Exercise\baby_value.jpg', v)

print(" Đã chuyển sang HSV và lưu 3 kênh: Hue, Saturation, Value.")
