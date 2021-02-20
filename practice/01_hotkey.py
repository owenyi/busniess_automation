import keyboard
import time

def loop():
    while True:
        if keyboard.is_pressed('p'):
            break
        print(1)
        time.sleep(1)
        print(2)
        time.sleep(2)

keyboard.add_hotkey('ctrl+-', lambda: loop()) # lambda : 함수 실행
keyboard.add_hotkey('ctrl+/', lambda: print("pause"))
keyboard.wait('esc') # esc 누르면 종료