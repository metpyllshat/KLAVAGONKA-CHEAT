import pyautogui
import cv2
import keyboard
import numpy as np
import pytesseract
import captcha

# [Settings]
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
pyautogui.FAILSAFE = False

def main():
    while True:
        if keyboard.is_pressed('insert'):
            area=(140,430,730,150)
            image = pyautogui.screenshot(region=area)
            
            img = np.array(image)
            #img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  

            #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            #gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]  # Бинаризация

            cv2.imwrite("processed.png", img)

            #text = pytesseract.image_to_string(gray, lang='rus')
            text = captcha.ocr_space_file("processed.png")
            text = text.replace('\n',' ')
            keyboard.write(text)

if __name__ == "__main__":
    main()