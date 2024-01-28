from pynput import keyboard
import time
import threading
import pyautogui

print('程序加载中', end='')
for i in range(5):
    print('.', end='')
    time.sleep(1)
print('开始运行')

isJ = False
timeMclick = 0
croodMclick = [0, 0, 0, 0]


def doJ():
    print('jump!')
    global isJ, croodMclick
    isJ = True
    length = ((croodMclick[3] - croodMclick[1]) ** 2 + (croodMclick[2] - croodMclick[0]) ** 2) ** 0.5
    timeCoe = 0.0028
    timeSleep = timeCoe * length
    time.sleep(0.5)
    print(timeSleep)
    pyautogui.mouseDown()
    time.sleep(timeSleep)
    pyautogui.mouseUp()
    print('stopjump')
    isJ = False


def on_press(key):
    global croodMclick, timeMclick, isJ
    print(key)
    if str(key) == "'j'" and not isJ:
        x, y = pyautogui.position()
        croodMclick[timeMclick * 2] = x
        croodMclick[timeMclick * 2 + 1] = y
        if timeMclick:
            threading.Thread(target=doJ).start()
        timeMclick = 1 if not timeMclick else 0
        print(x, y, timeMclick)


def listen_key_press():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


listen_key_press()