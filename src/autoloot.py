#!python
#cython: language_level=3

from pyautogui import locate, locateAll, pixelMatchesColor
from time import sleep
from mouse import drag, move, press, release, double_click
from lib.comon import screenContainer, configs, sortLeft

def autoloot(skipDrag=False):
    while not pixelMatchesColor(650, 1, (255, 255, 255)) or not pixelMatchesColor(1425, 60, (255, 255, 255)):
        sleep(.1)
    print("Autoloot > container found, checking for loot..")
    vincinity = screenContainer('vincinity')
    car = locate("./images/utils/car.jpg", vincinity, confidence=0.7, grayscale=True)
    found = []
    for name in range(25):
        result = locateAll("./images/autoloot/%s.jpg" % name, vincinity, confidence=0.9, grayscale=True)
        items = list(result)
        if len(items):
            found = found + items
    if len(found):
        found.sort(key=sortLeft, reverse=True)
        for item in found:
            if not car or skipDrag:
                move(item.left + configs['center']['x'] + 20, item.top + configs['center']['y'] + 20, absolute=True, duration=0.2)
                double_click()
            else:
                drag(item.left + configs['center']['x'] + 20, item.top + configs['center']['y'] + 20, car.left + configs['center']['x'] + 20, car.top + configs['center']['y'] + 20, absolute=True, duration=0.3)

