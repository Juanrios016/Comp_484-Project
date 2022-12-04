from pyboy import PyBoy
import numpy as np

pyboy = PyBoy('ROMs/Super Mario Land.gb')
while not pyboy.tick():
    pass
pyboy.stop()