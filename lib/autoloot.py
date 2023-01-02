from pyautogui import locate, locateAll, pixelMatchesColor
from time import sleep
from mouse import drag, move, double_click
from lib.comon import screenContainer, anchors, sortLeft

def autoloot(skipDrag=False):
    abordCount = 0
    while not pixelMatchesColor(anchors['whitePixels']['first']['x'], anchors['whitePixels']['first']['y'], (255, 255, 255)) or not pixelMatchesColor(anchors['whitePixels']['second']['x'], anchors['whitePixels']['second']['y'], (255, 255, 255)):
        sleep(.1)
        abordCount = abordCount + 1
        if abordCount > 40:
            print("Autoloot > Aborded, no container found")
            return
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
                move(item.left + anchors['center']['x'] + 20, item.top + anchors['center']['y'] + 20, absolute=True, duration=0.2)
                double_click()
            else:
                drag(item.left + anchors['center']['x'] + 20, item.top + anchors['center']['y'] + 20, car.left + anchors['center']['x'] + 20, car.top + anchors['center']['y'] + 20, absolute=True, duration=0.3)

