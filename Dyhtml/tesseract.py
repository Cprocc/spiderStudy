from pytesseract import *
from PIL import Image

pytesseract.tesseract_cmd = r"D:\zxc_D\Tesseract-OCR\tesseract.exe"


image = Image.open("test1.jpg")
text = image_to_string(image)
print(text)
