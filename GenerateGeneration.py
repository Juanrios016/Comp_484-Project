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

    def setParents(self, candidate, candidateFitness, chromosome):
        """Sets parents based on fitness score"""
        if candidateFitness > self.parent1Fitness - 5:
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

    def crossover1(self):
        child = MarioBrain()
        for i in range(len(child.actions)):
            #one and one chromosome
            if i % 2 == 0:
                child.actions[i][0] = self.parent1.actions[i][0]
            else:
                child.actions[i][0] = self.parent2.actions[i][0]
        return self.mutation(child)

    def crossover2(self):
        child = MarioBrain()
        minChrom = random.choice([int(self.parent1Chromosome * 0.85), int(self.parent2Chromosome * 0.85)])
        for i in range(minChrom):
            chroPar1Dis = self.parent1.actions[i][1]
            chroPar2Dis = self.parent2.actions[i][1]
            if chroPar1Dis > chroPar2Dis:
                child.actions[i][0] =  self.parent1.actions[i][0]
                child.actions[i][1] =  self.parent1.actions[i][1]
            elif chroPar1Dis < chroPar2Dis:
                child.actions[i][0] =  self.parent2.actions[i][0]
                child.actions[i][1] =  self.parent2.actions[i][1]
            else:
                child.actions[i][0] =  random.choice([self.parent2.actions[i][0], self.parent2.actions[i][0],
                                                      self.parent1.actions[i][0], self.parent1.actions[i][0],
                                                      self.parent1.actions[i][0], self.parent1.actions[i][0],
                                                      self.parent1.actions[i][0], random.randint(0, 10)])
                #child.actions[i][1] =  random.choice([self.parent1.actions[i][1], self.parent2.actions[i][1]])

        
            #else:
            #    mutateBoo = random.randint(0,9)
            #    if mutateBoo < 2 :
            #        child.actions[i][0] = random.randint(0, 10)
        

        return child


    def mutation(self, child: MarioBrain):
        """Allows 10 chromosomes to be changed, but only 5 before the parent1
        chromosome/ movement when it died (parent 2 can have a higher chromosome pos)"""
        for i in range(3000):
            mutateBoo = random.randint(0,19)
            if mutateBoo < 1:
                child.actions[i][0] = random.randint(0, 10)
        return child
    

    def computeNextGen(self):
        """Computes a new generation of 5 Marios"""
        nextGen = []
        for i in range(10):
            child = self.crossover2()
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

nextGen = testing.computeNextGen()

print("---------------------")
for i in nextGen:
    print(i.actions[0:50])
'''

