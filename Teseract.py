import pytesseract
import pyautogui
from pynput.keyboard import Key, Controller
import time
import googletrans
from googletrans import Translator


translator = Translator()
keyboard = Controller()
i = 1 

while i < 99999:
    myScreenshot = pyautogui.screenshot(region=( 140, 40 ,380, 60))
    myScreenshot.save(r'C:\Users\Duco\Desktop\gaming.png')
    time.sleep(3)
    pytesseract.pytesseract.tesseract_cmd = (r'C:\Program Files\Tesseract-OCR\tesseract')
    ##print(pytesseract.image_to_string(r'C:\Users\Duco\Desktop\gaming.png'))
    Valuable = pytesseract.image_to_string(r'C:\Users\Duco\Desktop\gaming.png')
    result = translator.translate(Valuable, src='german', dest='dutch')
    print(result.text)
    ##keyboard.type(Valuable)
    i +=1






##import pyautogui, sys
##print('Press Ctrl-C to quit.')
##try:
##    while True:
##        x, y = pyautogui.position()
##        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
##        print(positionStr, end='')
##        print('\b' * len(positionStr), end='', flush=True)
##except KeyboardInterrupt:
##    print('\n')
