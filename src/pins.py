#!python
#cython: language_level=3

from lib.unbox import unbox
from lib.comon import screenContainer, selectOption, exists, anchors, resolution
from time import sleep
from mouse import double_click, move
from pyautogui import locateAll, locate

def pins():
    sc = screenContainer('vincinity')
    bundle = locate("./images/%s/pins/crafted.jpg" % resolution, sc, confidence=0.97, grayscale=True)
    if bundle:
        move(anchors['vincinity']['x']+bundle.left+50, anchors['vincinity']['y']+bundle.top+5, absolute=True, duration=0.1)
        double_click()
        print("Lockpicks > Grabbing crafted bundle")
        sleep(2)
        return
    result = locateAll("./images/%s/pins/lock.jpg" % resolution, sc, confidence=0.97, grayscale=True)
    lockpicks = list(result)
    lockpicksCount = len(lockpicks)
    if (lockpicksCount >= 10):
        selectOption('vincinity', lockpicks[0].left, lockpicks[0].top, 6)
        print("Lockpicks > Crafting bundle")
        sleep(4)
        return
    else:
        result = locateAll("./images/%s/pins/pin.jpg" % resolution, sc, confidence=0.97, grayscale=True)
        pins = list(result)
        count = len(pins)
        if (count + lockpicksCount < 10):
            unbox('pins')
            return
        else:
            if exists(sc, 'vincinity', 'pins', 'pin', 6, 0.97):
                print("Lockpicks > Crafing lockpick")
                sleep(2.5)
                return