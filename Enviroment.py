import numpy as np
import sys
from pyboy import PyBoy, WindowEvent

fitnessScore = 0
class Environment:
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
        assert self.mario._level_progress_max == 0
        
        #statespace
        self.action_size = 5
        state_full = np.asarray(self.mario.game_area())
        np.append =(state_full, self.mario.level_progress)
        self.state_size = state_full.size
        
        
    def reset(self):
        """Resets game"""
        self.mario._level_progress_max = 0
        self.mario.reset_game()
        self.done = False
        self.pyboy.tick()
        assert self.mario.lives_left == 2
        state_full = np.asarray(self.mario.game_area())
        # np.append(state_full, self.mario.level_progress)  #broken rn with current lazy
        return state_full

    def render(self, i, feet_val, env):
        """Function that runs the game """
        while feet_val <= 350:
            env.pyboy.tick()
            i += 1
            if i > 60:
                break
        
        if feet_val >= 350:
            tempo = 2
            for _ in range(tempo):
                env.pyboy.tick()
    
    def step(self, action):
        """Inputs an action to be performed on Mario based on integer comming from
        MarioBrain class, which represent the brain
        
        **Note: We have a total of 16 possible buttons combination input including an
        input for not doing anything. We could possibly remove any combination that
        presses the ARROW_DOWN because it might not do anything. 
        Also, we might want to change the time for each input because that seems affects
        how fast mario performs each movement.
        """
        
        if action == 0:
            self.pyboy.send_input(WindowEvent.PRESS_BUTTON_A) #jump
            self.time = 1
        elif action == 1:
            self.pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT) #move right
            self.time = 5
        elif action == 2:
            self.pyboy.send_input(WindowEvent.PRESS_BUTTON_B) #run/fireball
            self.time = 50
        elif action == 3:
            self.pyboy.send_input(WindowEvent.PRESS_BUTTON_B) #fast jump
            self.pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
            self.time = 1
        elif action == 4:
            self.pyboy.send_input(WindowEvent.PRESS_BUTTON_B) #fast jump right
            self.pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT)
            self.pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
            self.time = 1
        elif action == 5:
            self.pyboy.send_input(WindowEvent.PRESS_BUTTON_B) #run right
            self.pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT)
            self.time = 50
        elif action == 6:
            self.pyboy.send_input(WindowEvent.PRESS_BUTTON_B) #run left
            self.pyboy.send_input(WindowEvent.PRESS_ARROW_LEFT)
            self.time = 50
        elif action == 7:
            self.pyboy.send_input(WindowEvent.PRESS_BUTTON_B) #fast jump left
            self.pyboy.send_input(WindowEvent.PRESS_ARROW_LEFT)
            self.pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
            self.time = 1
        elif action == 8:
            self.pyboy.send_input(WindowEvent.PRESS_ARROW_LEFT) #move left
            self.time = 5
        elif action == 9:
            self.pyboy.send_input(WindowEvent.PRESS_ARROW_DOWN) #crouch
            self.time = 5
        

    def releaseStep(self, action):
        """Releases current Mario's action based on MarioBrain's input"""
        if action ==0:
            self.pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)
            self.time = 50 
        elif action == 1:
            self.pyboy.send_input(WindowEvent.RELEASE_ARROW_RIGHT)
            self.time = 5
        elif action == 2:
            self.pyboy.send_input(WindowEvent.RELEASE_BUTTON_B)
            self.time = 1
        elif action == 3:
            self.pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)
            self.pyboy.send_input(WindowEvent.RELEASE_BUTTON_B)
            self.time = 1
        elif action == 4:
            self.pyboy.send_input(WindowEvent.RELEASE_ARROW_RIGHT)
            self.pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)
            self.pyboy.send_input(WindowEvent.RELEASE_BUTTON_B)
            self.time = 1
        elif action == 5:
            self.pyboy.send_input(WindowEvent.RELEASE_ARROW_RIGHT)
            self.pyboy.send_input(WindowEvent.RELEASE_BUTTON_B)
            self.time = 1
        elif action == 6:
            self.pyboy.send_input(WindowEvent.RELEASE_ARROW_LEFT)
            self.pyboy.send_input(WindowEvent.RELEASE_BUTTON_B)
            self.time = 1
        elif action == 7:
            self.pyboy.send_input(WindowEvent.RELEASE_ARROW_LEFT)
            self.pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)
            self.pyboy.send_input(WindowEvent.RELEASE_BUTTON_B)
            self.time = 1
        elif action == 8:
            self.pyboy.send_input(WindowEvent.RELEASE_ARROW_LEFT)
            self.time = 5
        elif action == 9:
            self.pyboy.send_input(WindowEvent.RELEASE_ARROW_DOWN)
            self.time = 5
    
    def getFitness(self):
        """Returns Mario's fitness"""
        global fitnessScore
        fitnessScore = self.mario.level_progress
        return fitnessScore

    
    