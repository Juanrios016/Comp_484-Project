import math
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
        #self.parent1Pos = 0
        self.parent2 = False
        self.parent2Fitness = 0
        self.parent2Chromosome = 0
       # self.parent2Pos = 0

    def getParents(self):
        """Return parents (two Marios) with highest fitness score"""
        return self.parent1, self.parent2
    
    def getFitnessScores(self):
        """Return parents'/brains' fitness score"""
        return self.parent1Fitness, self.parent2Fitness

    def setParents(self, candidate, candidateFitness, chromosome,):
        """Sets parents based on fitness score"""
        if candidateFitness > self.parent1Fitness :
            self.parent2 = self.parent1
            self.parent2Fitness = self.parent1Fitness
            self.parent2Chromosome =self.parent1Chromosome
            #self.parent2Pos = self.parent1Pos

            #self.parent1Pos = pos
            self.parent1 = candidate
            self.parent1Fitness = candidateFitness
            self.parent1Chromosome = chromosome

        elif candidateFitness == self.parent1Fitness and chromosome < self.parent1Chromosome:
            self.parent2 = self.parent1
            self.parent2Fitness = self.parent1Fitness
            self.parent2Chromosome =self.parent1Chromosome
            #self.parent2Pos =self.parent1Pos

            #self.parent1Pos = pos
            self.parent1 = candidate
            self.parent1Fitness = candidateFitness
            self.parent1Chromosome = chromosome

        elif candidateFitness > self.parent2Fitness:
            self.parent2 = candidate
            self.parent2Fitness = candidateFitness
            self.parent2Chromosome = chromosome
            #self.parent2Pos = pos

        elif candidateFitness == self.parent2Fitness and chromosome <self.parent2Chromosome:
            self.parent2 = candidate
            self.parent2Fitness = candidateFitness
            self.parent2Chromosome = chromosome
            #self.parent2Pos = pos
    
    
     #old versions of crossover 
    '''
    def crossover1(self, parent1, parent2):
        """Generates a child from parents chromosomes (Mario's movements) with the option
        of not changing any current chromosome that comes from initializing a new brain"""
        child = MarioBrain()
        for i in range(len(child.actions)):
            parChromosome = random.choice([parent1.actions[i], parent2.actions[i]])
            #keepParChrom = random.choice([True, False])
            #if keepParChrom: 
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

        return self.mutation(child)

    def crossover4(self, parent1, parent2):
        child = MarioBrain()
        choice = max(self.parent1Chromosome, self.parent2Chromosome)
        partition = random.randint(0, choice)

        for i in range(0,partition):
            child.actions[i] = parent1.actions[i]
        for i in range(partition, len(parent1.actions)):
            child.actions[i] = parent2.actions[i]

        return self.mutation(child)

    '''

    # new approaches (maybe)
    def crossover1(self, parent1, parent2):
        child = MarioBrain()
        #select a chromosome to partition movements 
        partitionChromose = random.randint(0, random.choice([self.parent1Chromosome-2, self.parent2Chromosome-2]))
        for i in range(partitionChromose):
            child.actions[i] = parent1.actions[i]
        for i in range(partitionChromose+1, len(child.actions)):
            child.actions[i] = parent2.actions[i]
        return self.mutation(child)

    def crossover2(self, parent1, parent2):
        child = MarioBrain()
        for i in range(len(child.actions)):
            #one and one chromosome
            if i % 2 == 0:
                child.actions[i] = parent1.actions[i]
            else:
                child.actions[i] = parent2.actions[i]
        return self.mutation(child)

    def nextGen2(self):
        """ handles the crossover and generates new marios in the same functions.
        Keeps 90 percent of the parent's chromosomes"""
        newGen = []
        for i in range(10):
            child = MarioBrain()
            parentChoice = random.choice(self.getParents())
            partition = random.choice([self.parent1Chromosome, self.parent2Chromosome])
            for i in range(partition-math.floor(0.10*partition)):
                child.actions[i] = parentChoice.actions[i]
            newGen.append(self.mutation(child))
        return newGen

    def nextGen3(self):
        """ handles the crossover and generates new marios in the same function.
        selects a parent who only Keeps 90 percent of the parent's chromosomes and selects a
        partition chromosome"""
        newGen = []
        for i in range(10):
            child = MarioBrain()
            #parentChoice = random.choice(self.getParents())
            #partition = random.choice([self.parent1Chromosome, self.parent2Chromosome])
            partitionChromose = random.randint(0, random.choice([(self.parent1Chromosome - math.floor(0.10*self.parent1Chromosome)), (self.parent2Chromosome - math.floor(0.10*self.parent2Chromosome))]))
            for i in range(partitionChromose):
                child.actions[i] = self.parent1.actions[i]
            for i in range(partitionChromose+1, len(child.actions)):
                child.actions[i] = self.parent2.actions[i]
            #for i in range(partition-math.floor(0.10*partition)):
            #    child.actions[i] = parentChoice.actions[i]
            newGen.append(self.mutation(child))
        return newGen


    def mutation(self, child: MarioBrain):
        """Allows 10 chromosomes to be changed, but only 5 before the parent1
        chromosome/ movement when it died (parent 2 can have a higher chromosome pos)"""
        limit = 0
        for i in range(3000):
            mutateBoo = random.randint(0,19)
            if mutateBoo == 0 and limit < 5 and i < self.parent1Chromosome:
                child.changeChromose(i)
                limit += 1
            elif  mutateBoo == 0 and limit < 10:
                child.changeChromose(i)
                limit += 1
        return child
    

    def computeNextGen(self, p1, p2):
        """Computes a new generation of 5 Marios"""
        nextGen = []
        for i in range(6):
            child = self.crossover1(p1, p2)
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
testing.parent1 = brain1
testing.parent1Chromosome = 20
testing.parent2 = brain2
testing.parent2Chromosome = 30

nextGen = testing.nextGen2()

print("---------------------")
for i in nextGen:
    print(i.actions[0:50])
'''

