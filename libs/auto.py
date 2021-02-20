from pyautogui import leftClick, typewrite
from keyboard import is_pressed

def autoSettings():
    while True:
        if is_pressed('end'):
            break
        leftClick(x=1919, y=1055, interval=1)
        leftClick(x=28, y=1056, interval=1)
        leftClick(x=33, y=943, interval=1)
        leftClick(x=1893, y=28, interval=1)
        leftClick(x=768, y=1061, interval=1)

def autoCmd():
    while True:
        if is_pressed('end'):
            break
        leftClick(x=232, y=1053, interval=1)
        typewrite(['c', 'm', 'd'], interval=0.2)
        typewrite(['enter'], interval=0.2)
        typewrite(['e', 'x', 'i', 't', 'enter'], interval=0.2)
