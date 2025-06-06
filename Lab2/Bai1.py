import cv2
import numpy as np
import os

def image_inverse(img):
    return 255 - img

def gamma_correction(img, gamma=2.2):
    normalized = img / 255.0
    corrected = np.power(normalized, gamma)
    return np.uint8(corrected * 255)

def log_transform(img):
    c = 255 / np.log(1 + np.max(img))
    return np.uint8(c * np.log(1 + img))

def histogram_equalization(img):
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.equalizeHist(img)

def contrast_stretching(img):
    a, b = np.min(img), np.max(img)
    stretched = (img - a) * (255 / (b - a))
    return np.uint8(stretched)

def apply_transformation(choice, image):
    if choice == 'I':
        return image_inverse(image)
    elif choice == 'G':
        return gamma_correction(image)
    elif choice == 'L':
        return log_transform(image)
    elif choice == 'H':
        return histogram_equalization(image)
    elif choice == 'C':
        return contrast_stretching(image)
    else:
        return image

def main():
    input_folder = r"D:\download\VanLangUni\HK243\Nhap mon xu ly anh so\lab2\exercise"
    output_folder = r"D:\download\VanLangUni\HK243\Nhap mon xu ly anh so\lab2\bai1"
    os.makedirs(output_folder, exist_ok=True)

    choices = {
        'I': 'Image Inverse',
        'G': 'Gamma Correction',
        'L': 'Log Transform',
        'H': 'Histogram Equalization',
        'C': 'Contrast Stretching'
    }

    print("Chọn 1 trong các phép biến đổi:")
    for k, v in choices.items():
        print(f"{k}: {v}")

    key = input("Nhập lựa chọn (I/G/L/H/C): ").upper()

    for filename in os.listdir(input_folder):
        path = os.path.join(input_folder, filename)
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if img is not None:
            processed = apply_transformation(key, img)
            out_path = os.path.join(output_folder, f"{key}_{filename}")
            cv2.imwrite(out_path, processed)
            print(f"Đã lưu: {out_path}")
            cv2.imshow("Kết quả", processed)
            cv2.waitKey(500)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
