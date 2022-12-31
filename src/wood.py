#!python
#cython: language_level=3

from lib.comon import screenContainer, exists
from time import sleep

def planks():
    sc = screenContainer('vincinity')
    for name in range(2):
        if exists(sc, 'vincinity', 'wood', name + 2, 4):
            print("Planks > Log found, chopping..")
            sleep(7)
            return

def sticks():
    sc = screenContainer('vincinity')
    for name in range(2):
        if exists(sc, 'vincinity', 'wood', name, 4):
            print("Sticks > Long stick found, chopping..")
            sleep(7)
            return
