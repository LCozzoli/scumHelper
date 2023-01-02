from keyboard import add_hotkey
from time import sleep
from lib.comon import keybinds, runningAction
from lib.wood import planks, sticks
from lib.pins import pins
from lib.unbox import unboxIt
from lib.autoclick import autoclick
from lib.autoloot import autoloot
from lib.utils import buyBulk, withdrawItems, moveItems

mode = "off"

def setMode(param):
    global mode
    mode = param
    print("Mode > %s" % param)

def checkLoot():
    global mode
    if mode == "autoloot":
        autoloot(True)

def switchUnbox():
    global mode
    mode = "nails" if mode == "bolts" else "bolts"
    print("Mode > unbox %s" % mode)

add_hotkey(keybinds['disable'], setMode, args=("off",))
add_hotkey(keybinds['sticks'], setMode, args=("sticks",))
add_hotkey(keybinds['planks'], setMode, args=("planks",))
add_hotkey(keybinds['unbox'], switchUnbox)
add_hotkey(keybinds['lockpicks'], setMode, args=("pins",))
add_hotkey(keybinds['autoclick'], setMode, args=("autoclick",))
add_hotkey(keybinds['autoloot'], setMode, args=("autoloot",))
add_hotkey(keybinds['buyBulk'], buyBulk)
add_hotkey(keybinds['withdraw'], withdrawItems)
add_hotkey(keybinds['moveItems'], moveItems)
add_hotkey(keybinds['useButton'], checkLoot)

def run():
    while True:
        if mode and not runningAction():
            try:
                if not runningAction():
                    if mode == "pins":
                        pins()
                    elif mode == "autoclick":
                        autoclick()
                    elif mode == "planks":
                        planks()
                    elif mode == "sticks":
                        sticks()
                    elif mode == "bolts" or mode == "nails":
                        unboxIt(mode)
                elif mode != "lockpick":
                    if mode == "planks" or mode == "sticks":
                        sleep(1)
                    sleep(2)
            except Exception as e:
                print(e)
                sleep(1)
        sleep(0.05)

