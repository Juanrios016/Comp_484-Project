import random
import numpy as np

class MarioBrain():
    """ This class computes a single Mario Brain """

    def __init__(self):
        """Creates an array of size 1000 with integers between 0 and 15 inclusive
        that represents the different movements for Mario"""
        self.actions = np.arange(1000) #array that holds Mario movements
        for i in range(self.actions.size): 
            chromosome = random.randint(0, 15)
            self.actions[i] = chromosome
        
    def get_actions(self):
        """Returns an array of integers between 0 and 15 inclusive"""
        return self.actions

    def changeChromose(self, pos):
        """Changes a single chromose"""
        self.actions [pos] = random.randint(0, 15)


    
        

#testing = MarioBrain()
#k = testing.get_actions()

#print(k[0:50])
