import cv2
import numpy as np


img = cv2.imread(r'd:\download\VanLangUni\HK243\Nhap mon xu ly anh so\lab1\Exercise\baby.jpeg')


if img is None:
    print(" Không đọc được ảnh! Kiểm tra lại đường dẫn hoặc tên ảnh.")
    exit()


zeros = np.zeros_like(img[:, :, 0])


cv2.imwrite(r'd:\download\VanLangUni\HK243\Nhap mon xu ly anh so\lab1\Exercise\baby_red.jpg',
            cv2.merge([zeros, zeros, img[:, :, 2]]))
cv2.imwrite(r'd:\download\VanLangUni\HK243\Nhap mon xu ly anh so\lab1\Exercise\baby_green.jpg',
            cv2.merge([zeros, img[:, :, 1], zeros]))
cv2.imwrite(r'd:\download\VanLangUni\HK243\Nhap mon xu ly anh so\lab1\Exercise\baby_blue.jpg',
            cv2.merge([img[:, :, 0], zeros, zeros]))

print(" Đã tạo xong 3 ảnh: đỏ, xanh lá, xanh dương.")
