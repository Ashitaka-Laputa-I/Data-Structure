import cv2
import easyocr
from PIL import Image


def preprocess_image(image_path):
    # 读取图像
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # 转换为灰度图像
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 应用二值化（阈值化）处理
    _, threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return threshold_image


def recognize_captcha(image_path):
    # 预处理图像
    preprocessed_image = preprocess_image(image_path)

    # 保存预处理后的图像（可选）
    cv2.imwrite('preprocessed_captcha.png', preprocessed_image)

    # 使用EasyOCR进行OCR识别
    reader = easyocr.Reader(['en'])
    result = reader.readtext(preprocessed_image)

    # 提取识别结果
    recognized_text = ''.join([res[1] for res in result])

    return recognized_text.strip()


# 测试代码
if __name__ == "__main__":
    image_path = 'captcha.png'  # 替换为你的验证码图像路径
    recognized_text = recognize_captcha(image_path)
    print(f"Recognized CAPTCHA text: {recognized_text}")
