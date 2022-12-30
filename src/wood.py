#!python
#cython: language_level=3

from lib.comon import screenContainer, exists
from time import sleep

def planks():
    sc = screenContainer('vincinity')
    for name in range(2):
        if exists(sc, 'vincinity', 'wood', name + 2, 4):
            sleep(5)
            return

def sticks():
    sc = screenContainer('vincinity')
    for name in range(2):
        if exists(sc, 'vincinity', 'wood', name, 4):
            sleep(5)
            return
