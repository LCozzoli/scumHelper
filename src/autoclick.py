#!python
#cython: language_level=3

from mouse import click
from random import randrange
from time import sleep

def autoclick():
    click()
    sleep(randrange(40,60) / 100)