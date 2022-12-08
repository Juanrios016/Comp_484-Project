from MarioBrain import MarioBrain
import random
import numpy as np

mutationChance = 0.2
possibleActions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
weights = [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]
weightsModified = [.12, .15, .01, .02, .27, .15, .1, .1, .03, .05]
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
            
    def mutate(self, child, position):
        """Mutates a single chromosome in a child"""
        child.actions[position] = np.random.choice(possibleActions, 1, p=weights)

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
    
    def crossover1(self, parent1, parent2):
        """Generates a child from parents chromosomes (Mario's movements) with the option
        of not changing any current chromosome that comes from initializing a new brain"""
        child = MarioBrain()
        for i in range(len(child.actions)):
            parChromosome = random.choice([parent1.actions[i], parent2.actions[i]])
            keepParChrom = random.choice([True, False])
            if keepParChrom: 
                child.actions[i] = parChromosome
        return child

    def crossover2(self, parent1, parent2):
        child = MarioBrain()
        choice = random.choice([self.parent1Chromosome, self.parent2Chromosome])
        maxNum = max([self.parent1Chromosome, self.parent2Chromosome])
        partition = random.randint(0,choice)

        for i in range(0,partition):
            child.actions[i] = parent1.actions[i]
        for i in range(partition, maxNum):
            child.actions[i] = parent2.actions[i]
        
        for i in range(1000):
            if random.random() <= mutationChance:
                self.mutate(child, i)

        return child

    def crossover3(self, parent1, parent2):
        child = MarioBrain()
        choice = random.choice([self.parent1Chromosome, self.parent2Chromosome])   

        for i in range(choice):
            parChromosome = random.choice([parent1.actions[i], parent2.actions[i]])
            
            child.actions[i] = parChromosome
        return child    

    def crossover4(self, parent1, parent2):
        child = MarioBrain()
        choice = random.choice([self.parent1Chromosome, self.parent2Chromosome])
        partition = random.randint(0, choice)

        for i in range(0,partition):
            child.actions[i] = parent1.actions[i]
        for i in range(partition, len(parent1.actions)):
            child.actions[i] = parent2.actions[i]

        return child

    def crossover5(self, parent1, parent2):
        """Generates a child from parents chromosomes (Mario's movements) with the option
        of not changing any current chromosome that comes from initializing a new brain"""
        child = MarioBrain()

        choice = random.choice([self.parent1Chromosome, self.parent2Chromosome])
        partition = random.randint(0, choice)
        changesNum = random.randint(0, choice)


        for i in range(choice):
            parChromosome = random.choice([parent1.actions[i], parent2.actions[i]])
            notKeepParChrom = random.choice([True, False])
            if notKeepParChrom and i != changesNum: 
                child.actions[i] = parChromosome
        return child

    def crossover6(self, parent1, parent2):
        """Generates a child from parents chromosomes (Mario's movements) with the option
        of not changing any current chromosome that comes from initializing a new brain"""
        child = MarioBrain()

        choice = random.choice([self.parent1Chromosome, self.parent2Chromosome])
        partition = random.randint(0, choice)
        changesNum = random.randint(0, choice)


        for i in range(choice):
            parChromosome = random.choice([parent1.actions[i], parent2.actions[i]])
            keepParChrom = random.choice([True, False])
            if keepParChrom == False and i < changesNum:
                continue
            elif keepParChrom and i >= changesNum: 
                child.actions[i] = parChromosome
            
        return child

    
    def crossoverV2(self, parent1, parent2):
        """Generates a child from parents chromosomes (Mario's movements)"""
        child = MarioBrain()
        for i in range(len(child.actions)):
            parChromosome = random.choice([parent1.actions[i], parent2.actions[i]])
            keepParChrom = random.choice([True, False])
            if keepParChrom: 
                child.actions[i] = parChromosome
            if random.random() < mutationChance:
                self.mutate(child, i)
        return child

    def computeNextGen(self, p1, p2):
        """Computes a new generation of 5 Marios"""
        nextGen = []
        for i in range(5):
            child = self.crossover(p1, p2)
            nextGen.append(child)
        return nextGen
    
    def mutateComputeNextGen(self, p1, p2):
        """Computes a new generation of 5 Marios with the option of mutating a chromosome"""
        nextGen = []
        for i in range(10):
            child = self.crossover2(p1, p2)
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
