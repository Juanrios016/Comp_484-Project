import random
import numpy as np

possibleActions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
weights = [.12, .15, .01, .02, .32, .2, .05, .05, .03, .05]
class MarioBrain():
    """ This class computes a single Mario Brain """

    def __init__(self):
        """Creates an array of size 1000 with integers between 0 and 15 inclusive
        that represents the different movements for Mario"""
        self.actions = np.arange(1000) #array that holds Mario movements
        self.actions = np.random.choice(possibleActions, 1000, p=weights) #randomly assigns actions to the array
        
    def get_actions(self):
        """Returns an array of integers between 0 and 15 inclusive"""
        return self.actions

    def changeChromose(self, pos):
        """Changes a single chromose"""
        self.actions [pos] = random.randint(0, 9)

    def saveActions(self, fileName):
        """Saves the actions array to a file in a new folder called 'actions'"""
        np.savetxt(fileName, self.actions, fmt='%d', delimiter=',')

    def loadActions(self, fileName):
        """Loads the actions array from a file"""
        self.actions = np.loadtxt(fileName, delimiter=',')
    
    


    
        

#testing = MarioBrain()
#k = testing.get_actions()

#print(k[0:50])
