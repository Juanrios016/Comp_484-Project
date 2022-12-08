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
    def crossover1(self, parent1, parent2):
        child = MarioBrain()
        partitionChromose = random.randint(0, random.choice([self.parent1Chromosome-2, self.parent2Chromosome-2]))
        for i in range(partitionChromose):
            child.actions[i] = parent1.actions[i]
        for i in range(partitionChromose+1, len(child.actions)):
            child.actions[i] = parent2.actions[i]
        return self.mutation(child)

    def crossover2(self, parent1, parent2):
        child = MarioBrain()
        for i in range(len(child.actions)):
            '''
            if i-2 == self.parent1Chromosome or i-2 == self.parent2Chromosome:
               #print(child.actions[i-2])
               child.actions[i-2] = random.randint(0, 15)
               #print(child.actions[i-2])
            '''
            if i-1 == self.parent1Chromosome or i-1 == self.parent2Chromosome: # for changing the last i-1 movement for contunity
               child.actions[i-1] = random.randint(0, 15)
            elif i == self.parent1Chromosome or i == self.parent2Chromosome: # for changing the last i movement for contunity
               child.actions[i] = random.randint(0, 15)
            elif i % 2 == 0:
                child.actions[i] = parent1.actions[i]
            else:
                child.actions[i] = parent2.actions[i]
        return self.mutation(child)


    def mutation(self, child: MarioBrain):
        for i in range(1000):
            mutateBoo = random.randint(0,14)
            if mutateBoo == 0:
                child.changeChromose(i)
        return child
    

    def computeNextGen(self, p1, p2):
        """Computes a new generation of 5 Marios"""
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
