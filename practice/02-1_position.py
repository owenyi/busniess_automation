import pyautogui
from time import sleep

f = open("position.txt", "w")

sleep(4)
data = pyautogui.position()
print(data)
f.write(str(data))
sleep(4)
data = pyautogui.position()
print(data)
f.write(str(data))
sleep(4)
data = pyautogui.position()
print(data)
f.write(str(data))
sleep(4)
data = pyautogui.position()
print(data)
f.write(str(data))

f.close()