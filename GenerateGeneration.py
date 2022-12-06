from MarioBrain import MarioBrain
import random

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
        if candidateFitness > self.parent1Fitness :
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

    def crossover(self, parent1, parent2):
        """Generates a child from parents chromosomes (Mario's movements) with the option
        of not changing any current chromosome that comes from initializing a new brain"""
        child = MarioBrain()
        for i in range(len(child.actions)):
            parChromosome = random.choice([parent1.actions[i], parent2.actions[i]])
            keepParChrom = random.choice([True, False])
            if keepParChrom: 
                child.actions[i] = parChromosome
        return child

    def computeNextGen(self, p1, p2):
        """Computes a new generation of 5 Marios"""
        nextGen = []
        for i in range(5):
            child = self.crossover(p1, p2)
            nextGen.append(child)
        return nextGen

    def resetParents(self):
        self.parent1 = False
        self.parent1Fitness = 0
        self.parent2 = False
        self.parent2Fitness = 0
        
'''

brain1 = MarioBrain()
brain2 = MarioBrain()

testing = GenerateGeneration()
nextGen = testing.computeNextGen(brain1, brain2)

print("---------------------")
for i in range(5):
    print(nextGen[i].actions[0:50])

'''
