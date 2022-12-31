#!python
#cython: language_level=3

from lib.unbox import unbox
from lib.comon import screenContainer, selectOption, exists, configs
from time import sleep
from mouse import double_click, move
from pyautogui import locateAll, locate

def pins():
    sc = screenContainer('vincinity')
    bundle = locate("./images/pins/crafted.jpg", sc, confidence=0.97, grayscale=True)
    if bundle:
        move(configs['vincinity']['x']+bundle.left+50, configs['vincinity']['y']+bundle.top+5, absolute=True, duration=0.1)
        double_click()
        print("Lockpicks > Grabbing crafted bundle")
        sleep(2)
        return
    result = locateAll("./images/pins/lock.jpg", sc, confidence=0.97, grayscale=True)
    lockpicks = list(result)
    lockpicksCount = len(lockpicks)
    if (lockpicksCount >= 10):
        selectOption('vincinity', lockpicks[0].left, lockpicks[0].top, 6)
        print("Lockpicks > Crafting bundle")
        sleep(4)
        return
    else:
        result = locateAll("./images/pins/pin.jpg", sc, confidence=0.97, grayscale=True)
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