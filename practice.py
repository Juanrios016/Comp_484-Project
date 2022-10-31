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



classes = 10
batch_size = 64
population = 5
generations = 5
threshold = 100000


games = 800
time_h = 0
lucro = 0
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
        # np.append(state_full, self.mario.level_progress)  #broken rn with current lazy
        
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
    
    
class Network():
    
    def __init__(self):
        self.actions = []
        self.generation = 0
        
        for i in range(games):
            self.action = random.randint(0, 5)
            self.actions.append(self.action)
        self.lucro = 0
        
    def get_action(self):
        return self.actions
    
    def set_actions(self, actions, lucro):
        self.actions = actions
        self.lucro = lucro
        return self.lucro
    
    
def main():
    network = Network()
    env = environment()
    state_size = env.state_size
    action_size = env.action_size
    state = env.reset()
    state = np.reshape(state, [1, state_size])
    actions = network.get_action()
    
    for act in actions:
        try:
            filteredMario = [x for x in list(state[0]) if (x > 10 and x < 30)]
            
            index_mario = list(state[0]).index(filteredMario[0])
            feet_val = state[0][index_mario + 20]
            
        except:
            break
    
        act, tempo = env.step(act)
        
        state = np.asarray(env.mario.game_area())
        position = env.mario.level_progress
        state = np.reshape(state, [1, state_size])
        
        i = 0
        
        while feet_val <= 350:
            env.pyboy.tick()
            i += 1
            if i > 60:
                break
        
        if feet_val >= 350:
            tempo = 2
            for _ in range(tempo):
                env.pyboy.tick()
        
if __name__ == '__main__':
    main()

    