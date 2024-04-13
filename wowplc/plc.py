import cv2
import numpy as np
import time
import pyautogui
import random

from PIL import ImageGrab

average = [0, ]

tmp = cv2.imread('lure.png', 0) 
print ('get lure png')
w, h = tmp.shape[::-1]

duration_seconds = 0.2
print ('relax 4sec')
time.sleep(2)

for _ in range(1000):
    print(f"try number {_}")
    sleep_time = random.uniform(0, 2) + 3.5
    print(f'relax {sleep_time}')
    time.sleep(sleep_time)
    print('use pole')
    pyautogui.press('q')
    time.sleep(2)

    base_screen = ImageGrab.grab()
    print('save screen')
    base_screen.save('base_screen.png')

    img_rgb = cv2.imread('base_screen.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img_gray, tmp, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.7) 
    print ('GOGOOGO FISH')

    for i in range(200):
        time.sleep(0.1)
        try:
            clean_screen = ImageGrab.grab(bbox=(x,y,x+w,y+h))
            mean = np.mean(clean_screen)
            diff = average[-1] - mean
            print (diff)
            if diff >= 3:
                random_float = random.uniform(0, 0.7)
                pyautogui.moveTo(x+22, y+20, duration=(duration_seconds+random_float))
                time.sleep(0.2 + (random_float/2))
                pyautogui.rightClick()
                break
            average.append(mean)
            if i == 195:
                clean_screen.save('clean_screen.png')

        except:
            print ("Cant grab lure image")
            for pt in zip(*loc[::-1]):
                x = int(pt[0])
                y = int(pt[1])
    try:
        del(x)
        del(y)
    except:
        pass
    average = [0, ]
