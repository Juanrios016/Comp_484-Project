import math
from MarioBrain import MarioBrain
import random
import numpy as np

possibleActions = [0,   1,   2,   3,   4,   5,   6,   7,   8,   9,   10 ]
rightWeighted =   [.10, .14, .02, .03, .33, .10, .03, .02, .02, .01,  .20]
mutationChance = 0.25 

class GenerateGeneration:
    """ This class is responsible for the creation of new generation of Marios
    for the emulator based on previous generations"""
    

    def __init__(self):
        """sets up the parents and their fitness score """
        self.parent1 = False
        self.parent1Fitness = 0
        self.parent1Chromosome = 0
        self.parent2 = False
        self.parent2Fitness = 0
        self.parent2Chromosome = 0

    def getParents(self):
        """Return parents (two Marios) with highest fitness score"""
        return self.parent1, self.parent2
    
    def getFitnessScores(self):
        """Return parents'/brains' fitness score"""
        return self.parent1Fitness, self.parent2Fitness

    def setParents(self, candidate, candidateFitness, chromosome):
        """Sets parents based on fitness score"""
        if candidateFitness > self.parent1Fitness:
            self.parent2 = self.parent1
            self.parent2Fitness = self.parent1Fitness
            self.parent2Chromosome =self.parent1Chromosome
            self.parent1 = candidate
            self.parent1Fitness = candidateFitness
            self.parent1Chromosome = chromosome

        elif candidateFitness == self.parent1Fitness and chromosome < self.parent1Chromosome:
            self.parent2 = self.parent1
            self.parent2Fitness = self.parent1Fitness
            self.parent2Chromosome =self.parent1Chromosome
            self.parent1 = candidate
            self.parent1Fitness = candidateFitness
            self.parent1Chromosome = chromosome

        elif candidateFitness > self.parent2Fitness:
            self.parent2 = candidate
            self.parent2Fitness = candidateFitness
            self.parent2Chromosome = chromosome

        elif candidateFitness == self.parent2Fitness and chromosome <self.parent2Chromosome:
            self.parent2 = candidate
            self.parent2Fitness = candidateFitness
            self.parent2Chromosome = chromosome

    def resetParents(self):
        self.parent1 = False
        self.parent1Fitness = 0
        self.parent2 = False
        self.parent2Fitness = 0

    def crossover(self):
        """ Computes a child who prioritizes parent 1 but ther is a 0.50 chance to generate 
        a child based on parent1 or parent2 chromosome number. It selects a the chromosomes form both 
        parents who has the highest distance"""
        child = MarioBrain()
        choice = random.choice([self.parent1Chromosome, self.parent2Chromosome])
        lastChrom = int(choice) - 6 #afeter it dies, it takes around 3-4movements to restrat. For continuity, we do -6
        for i in range(0, lastChrom):
            chroPar1Dis = self.parent1.actions[i][1]
            chroPar2Dis = self.parent2.actions[i][1]
            if chroPar1Dis > chroPar2Dis: 
                child.actions[i][0] =  self.parent1.actions[i][0]
                child.actions[i][1] =  self.parent1.actions[i][1]
            elif chroPar1Dis < chroPar2Dis:
                child.actions[i][0] =  self.parent2.actions[i][0]
                child.actions[i][1] =  self.parent2.actions[i][1]
            else:
                #weighted parent 1 more because we want more child like it. Mostly for cases where position is the same
                child.actions[i][0] =  random.choice([self.parent1.actions[i][0],
                                                        self.parent2.actions[i][0], 
                                                        np.random.choice(possibleActions, p=rightWeighted)],
                                                        1, p=(0.6, 0.3, 0.1))
        
        return self.mutate(child, lastChrom)

    def mutate(self, child, start):
        """Mutates a single chromosome in a child"""
        for i in range(start, len(child.actions)):
            child.actions[i][0] = np.random.choice(possibleActions, 1, p=rightWeighted)
        return child

    def mutateComputeNextGen(self):
        """Computes a new generation of 5 Marios with the option of mutating a chromosome"""
        nextGen = []
        child = MarioBrain()
        for i in range(10):
            child = self.crossover()
            nextGen.append(child)
        return nextGen
    
        

'''
brain1 = MarioBrain()
brain2 = MarioBrain()

testing = GenerateGeneration()
testing.parent1 = brain1
testing.parent1Chromosome = 20
testing.parent2 = brain2
testing.parent2Chromosome = 30

nextGen = testing.computeNextGen()

print("---------------------")
for i in nextGen:
    print(i.actions[0:50])
    
'''
