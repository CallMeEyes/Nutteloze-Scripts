import time
from pynput.keyboard import Key, Controller

keyboard = Controller()
i = 1
count = 1

name = input("Enter your tweet to be spammed: ")
time.sleep(10)

while i < 999:
        time.sleep(1)
        keyboard.type(str(name)+ " " + str(count) )
        keyboard.press(Key.cmd)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        keyboard.release(Key.cmd)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        count = count+1

#Gaming2020 12
                        
