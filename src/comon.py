#!python
#cython: language_level=3

from pyautogui import size, locateAll, pixelMatchesColor, screenshot
from mouse import move, click, right_click
from time import sleep
from json import loads
from random import choice

f = open ('config.json', "r")
configs = loads(f.read())

size = size()
action = {
    'x': int(size.width/2),
    'y': int(size.height/2 - configs['action'])
}

def sortLeft(elem):
    return elem.left

def selectOption(container, x, y, number, timeout=2):
    move(x=configs[container]['x']+x+10, y=configs[container]['y']+y+configs['buttons'], absolute=True, duration=0)
    right_click()
    move(configs[container]['x']+x+100, configs[container]['y']+y+configs['buttons']+20*number-10, absolute=True, duration=0.2)
    click()
    sleep(timeout)

def exists(sc, container, category, name, option, confid=0.97, timeout=2, randomChoice=True):
    res = locateAll("./images/%s/%s.jpg" % (category, name), sc, confidence=confid, grayscale=True)
    found = list(res)
    if len(found):
        exists = choice(found) if randomChoice else found[0]
        selectOption(container, exists.left, exists.top, option, timeout)
        return True
    return False

def runningAction():
    return pixelMatchesColor(action['x'], action['y'], (255, 255, 255), tolerance=10)

def screenContainer(container):
    return screenshot(region=(configs[container]['x'], configs[container]['y'], configs[container]['width'], configs[container]['height']))