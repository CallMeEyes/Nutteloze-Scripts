import pyperclip
import clipboard
from pynput import keyboard
from pynput.keyboard import Key, Listener

COMBINATIONS = [
    {keyboard.Key.shift, keyboard.Key.space},
]


current = set()

def execute():
    url = clipboard.paste()
    link = url[32:44]
    linkf = ("youtube.com/embed/" + link)
    pyperclip.copy(linkf)

    
    
def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()



