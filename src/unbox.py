#!python
#cython: language_level=3

from lib.comon import screenContainer, exists, configs
from mouse import drag, move, double_click
from pyautogui import locate, locateAll
from time import sleep

def lootStack(name):
    sc = screenContainer('vincinity')
    stacked = locate("./images/%s/stacked.jpg" % name, sc, confidence=0.97, grayscale=True)
    if stacked:
        move(configs['vincinity']['x']+stacked.left+50, configs['vincinity']['y']+stacked.top+5, absolute=True, duration=0.1)
        double_click()
        print("Unboxing > Looting %s stack" % name)
        sleep(2)
        return True
    return False

def stackUp(name):
    sc = screenContainer('vincinity')
    result = locateAll("./images/%s/item.jpg" % name, sc, confidence=0.9, grayscale=True)
    items = list(result)
    if len(items):
        first = items.pop(0)
        for item in items:
            drag(item.left + configs['vincinity']['x'] + 20, item.top + configs['vincinity']['y'] + 20, first.left + configs['vincinity']['x'] + 20, first.top + configs['vincinity']['y'] + 20, absolute=True, duration=0.2)

def unbox(name):
    sc = screenContainer('inventory')
    if exists(sc, 'inventory', name, 'box', 7, .7, False):
        print("Unboxing > Getting %s.." % name)
        sleep(2)
        return True
    return False

def unboxIt(name):
    if not lootStack(name):
        stackUp(name)
        unbox(name)
