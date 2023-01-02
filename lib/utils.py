from pyautogui import position, locate, locateAll, pixelMatchesColor
from mouse import drag, move, double_click, click
from time import sleep
from lib.comon import screenContainer, anchors, resolution

def buyBulk():
    print("Bulk Buy > clicking 15 times")
    for i in range(15):
        click()
        sleep(0.02)

def withdrawItems():
    sc = screenContainer('depot')
    result = locateAll("./images/%s/utils/bought.jpg" % resolution, sc, confidence=0.90, grayscale=True)
    items = list(result)
    count = len(items)
    if count:
        print("Withdraw > found %s items to withdraw" % count)
        for item in items:
            move(item.left + anchors['depot']['x'] - 10, item.top + anchors['depot']['y'] - 10, absolute=True, duration=0.1)
            double_click()
            sleep(0.05)

def withdrawItem(name):
    sc = screenContainer('depot')
    result = locateAll("./images/%s/utils/%s.jpg" % (resolution, name), sc, confidence=0.90, grayscale=True)
    items = list(result)
    count = len(items)
    if count:
        print("Withdraw > found %s items to withdraw" % count)
        for item in items:
            move(item.left + anchors['depot']['x'] + 20, item.top + anchors['depot']['y'] + 20, absolute=True, duration=0.1)
            double_click()
            sleep(0.05)

def moveItems():
    center = screenContainer('center')
    crate = locate("./images/%s/utils/greenbox.jpg" % resolution, center, confidence=0.7, grayscale=True)
    if crate:
        x, y = position()
        inventory = screenContainer('inventory')
        result = locateAll("./images/%s/utils/selecteditem.jpg" % resolution, inventory, confidence=0.8, grayscale=True)
        items = list(result)
        count = len(items)
        found = False
        if count:
            print("Move > found %s items to move" % count)
            for item in items:
                if pixelMatchesColor(int(anchors['inventory']['x'] + item.left), int(anchors['inventory']['x'] + item.top), (78, 0, 10)):
                    found = True
                    drag(anchors['inventory']['x'] + item.left - 20, anchors['inventory']['x'] + item.top + 20, crate.left + anchors['center']['x'] - 20, crate.top + anchors['center']['y'] + 20, absolute=True, duration=0.2)
        if not found:
            drag(x, y, crate.left + anchors['center']['x'] - 20, crate.top + anchors['center']['y'] + 20, absolute=True, duration=0.2)
        move(x, y, absolute=True, duration=0.1)
