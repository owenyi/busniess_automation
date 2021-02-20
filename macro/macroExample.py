import keyboard
from libs.auto import autoSettings, autoCmd

keyboard.add_hotkey('ctrl+-', lambda: autoSettings()) # lambda : 함수 실행
keyboard.add_hotkey('ctrl+*', lambda: autoCmd())
keyboard.wait('esc')