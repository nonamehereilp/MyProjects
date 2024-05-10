import pyautogui
import pytesseract
from PIL import ImageGrab
import clipboard
import time

clipboard.copy('')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

pyautogui.hotkey('win', 'shift', 's')

run = True
while run:
    clipboard_image = ImageGrab.grabclipboard()
    
    if clipboard_image is not None:
        text = pytesseract.image_to_string(clipboard_image)
        print(text)
        clipboard.copy(text)
        run = False
    else: time.sleep(0.1)
