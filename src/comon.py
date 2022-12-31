#!python
#cython: language_level=3

from pyautogui import size, locateAll, pixelMatchesColor, screenshot
from mouse import move, click, right_click
from time import sleep
from json import loads
from random import choice

f = open ('config.json', "r")
configs = loads(f.read())

f = open ('resolutions.json', "r")
resolutions = loads(f.read())

resolution = configs["resolution"]
keybinds = configs["keybinds"]
anchors = resolutions[resolution]

size = size()
action = {
    'x': int(size.width/2),
    'y': int(size.height/2 - anchors['action'])
}

def sortLeft(elem):
    return elem.left

def selectOption(container, x, y, number):
    move(x=anchors[container]['x']+x+10, y=anchors[container]['y']+y+anchors['buttons'], absolute=True, duration=0)
    right_click()
    move(anchors[container]['x']+x+100, anchors[container]['y']+y+anchors['buttons']+20*number-10, absolute=True, duration=0.2)
    click()

def exists(sc, container, category, name, option, confid=0.97, randomChoice=True):
    res = locateAll("./images/%s/%s/%s.jpg" % (resolution, category, name), sc, confidence=confid, grayscale=True)
    found = list(res)
    if len(found):
        exists = choice(found) if randomChoice else found[0]
        selectOption(container, exists.left, exists.top, option)
        return True
    return False

def runningAction():
    return pixelMatchesColor(action['x'], action['y'], (255, 255, 255), tolerance=10)

def screenContainer(container):
    return screenshot(region=(anchors[container]['x'], anchors[container]['y'], anchors[container]['width'], anchors[container]['height']))