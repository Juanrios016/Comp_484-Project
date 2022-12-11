import random
import numpy as np

class MarioBrain():
    """ This class computes a single Mario Brain """

    def __init__(self):
        """Creates a 2D array of size 3000 with integers between 0 and 10 inclusive
        that represents the different movements for Mario
        [movement] [distance]
        """
        self.actions = np.eye(3000,2) #array that holds Mario movements
        for i in range(3000): 
            chromosome = random.randint(0, 10)
            self.actions[i][0] = chromosome
        
    def get_actions(self):
        """Returns an array of integers between 0 and 15 inclusive"""
        return self.actions

    def changeChromose(self, pos):
        """Changes a single chromose"""
        self.actions [pos][0] = random.randint(0, 10)

    def saveActions(self, fileName):
        """Saves the actions array to a file"""
        np.savetxt(fileName, self.actions, fmt='%d', delimiter=',')

    def loadActions(self, fileName):
        """Loads the actions array from a file"""
        self.actions = np.loadtxt(fileName, delimiter=',')
    
    
    
        
'''
testing = MarioBrain()
k = testing.get_actions()

print(k[10][1])
testing.setDistance(10, 566)
print(testing.getDistance(10))
'''



