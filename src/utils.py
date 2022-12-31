#!python
#cython: language_level=3

from pyautogui import position, locate, locateAll, pixelMatchesColor
from mouse import drag, move, double_click, click
from time import sleep
from lib.comon import screenContainer, configs, exists, selectOption, sortLeft

def buyBulk():
    for i in range(15):
        click()
        sleep(0.02)

def withdrawItems():
    sc = screenContainer('depot')
    result = locateAll("./images/utils/bought.jpg", sc, confidence=0.90, grayscale=True)
    items = list(result)
    count = len(items)
    if count:
        for item in items:
            move(item.left + configs['depot']['x'] - 10, item.top + configs['depot']['y'] - 10, absolute=True, duration=0.1)
            double_click()
            sleep(0.05)

def withdrawItem(name):
    sc = screenContainer('depot')
    result = locateAll("./images/utils/%s.jpg" % name, sc, confidence=0.90, grayscale=True)
    items = list(result)
    count = len(items)
    if count:
        for item in items:
            move(item.left + configs['depot']['x'] + 20, item.top + configs['depot']['y'] + 20, absolute=True, duration=0.1)
            double_click()
            sleep(0.05)

def moveItems():
    center = screenContainer('center')
    crate = locate("./images/utils/greenbox.jpg", center, confidence=0.7, grayscale=True)
    if crate:
        x, y = position()
        inventory = screenContainer('inventory')
        result = locateAll("./images/utils/selecteditem.jpg", inventory, confidence=0.8, grayscale=True)
        items = list(result)
        count = len(items)
        found = False
        if count:
            for item in items:
                if pixelMatchesColor(int(configs['inventory']['x'] + item.left), int(configs['inventory']['x'] + item.top), (78, 0, 10)):
                    found = True
                    drag(configs['inventory']['x'] + item.left - 20, configs['inventory']['x'] + item.top + 20, crate.left + configs['center']['x'] - 20, crate.top + configs['center']['y'] + 20, absolute=True, duration=0.2)
        if not found:
            drag(x, y, crate.left + configs['center']['x'] - 20, crate.top + configs['center']['y'] + 20, absolute=True, duration=0.2)
        move(x, y, absolute=True, duration=0.1)
