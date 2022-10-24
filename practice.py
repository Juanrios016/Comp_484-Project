import numpy as np
import matplotlib.pyplot as plt
import pickle
from matplotlib import style
import time
import pandas as pd
import random
import os
import sys
from pyboy import PyBoy, WindowEvent
import json

pyboy = PyBoy('ROMs/Super Mario Land.gb')
while not pyboy.tick():
    pass
pyboy.stop()