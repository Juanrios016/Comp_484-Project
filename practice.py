import re
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

class environment:
    def __init__(self):
        #setup to run the game
        fileName = 'ROMs/Super Mario Land.gb'
        quiet = "--quiet" in sys.argv
        self.pyboy = PyBoy(fileName, window_type="headless" if quiet else "SDL2", window_scale=5, debug=quiet, game_wrapper=True)
        self.pyboy.set_emulation_speed(1)
        assert self.pyboy.cartridge_title() == "SUPER MARIOLAN"
        
        #game wrapper to help with hooking into the game
        self.mario = self.pyboy.game_wrapper()
        self.mario.start_game()
        self.done = False
        self.time = 10
        
        #makes sure game variables are probably set
        assert self.mario.score == 0
        assert self.mario.lives_left == 2
        assert self.mario.world == (1, 1)
        assert self.mario.fitness == 0
        
        #statespace
        self.action_size = 5
        state_full = np.asarray(self.mario.game_area())
        np.append =(state_full, self.mario.level_progress)
        self.state_size = state_full.size
        
        
    def reset(self):
        self.mario.reset_game()
        self.done = False
        self.pyboy.tick()
        
        assert self.mario.lives_left == 2
        
        state_full = np.asarray(self.mario.game_area())
        np.append(state_full, self.mario.level_progress)
        
        return state_full
    
    def step(self, action):
        if action == 0:
            self.pyboy.send_input(WindowEvent.PRESS_BUTTON_A) # jump
            self.time = 50
        elif action == 1:
            self.pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT) #move right
            self.time = 5
        elif action == 2:
            self.pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)#release jump
            self.time = 5
        elif action == 3:
            self.pyboy.send_input(WindowEvent.RELEASE_ARROW_RIGHT)#stop moving right
            self.time = 5
        elif action == 4:
            self.pyboy.send_input(WindowEvent.PRESS_ARROW_LEFT)#move left
            self.time == 5
        return action, self.time
    
    
        
        



    