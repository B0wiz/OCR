import cv2
import pytesseract

image_path = 'temp/bw_image.jpg'
# image_path = 'form_image/1.jpg'
image = cv2.imread(image_path)

custom_config = r'-l tha+eng --psm 3'
text = pytesseract.image_to_string(image, config=custom_config)
print(text)