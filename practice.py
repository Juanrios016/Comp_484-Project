from pyboy import PyBoy, WindowEvent
import numpy as np

pyboy = PyBoy('ROMs/Super Mario Land.gb')
pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT)
while not pyboy.tick():
    pass
pyboy.stop()