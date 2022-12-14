import numpy as np
import os
import matplotlib.pyplot as plt
import time
from MarioBrain import MarioBrain
from GenerateGeneration import GenerateGeneration
from Enviroment import Environment


mutationChance = 0.2
possibleActions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
weights = [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]
rightWeighted = [.15, .2, .02, .03, .25, .17, .07, .05, .05, .01]
weightsModified = [.12, .15, .01, .02, .27, .15, .1, .1, .03, .05]

# level complete at position 2601
def individualEnvBehavior():
    """could be implememnted to run individual emulators at the same time"""
    pass



def main():
    parents = GenerateGeneration()
    trials = [] # for testing
    plotDataGenerations = []
    plotDataHighestPosition = []
    marioNumber = 0 # current Mario -for testing
    mario1 = MarioBrain()
    mario2 = MarioBrain()
    mario3 = MarioBrain()
    mario4 = MarioBrain()
    mario5 = MarioBrain()
    mario6 = MarioBrain()
    mario7 = MarioBrain()
    mario8 = MarioBrain()
    mario9 = MarioBrain()
    mario10 = MarioBrain()
    intitialPopualation = [mario1, mario2, mario3, mario4, mario5, mario6, mario7, mario8, mario9, mario10]

    allscores = [] #for testing to se if fitness score improves for each generation

    env = Environment() # using only one enviroment to run enverything
    env.pyboy.set_emulation_speed(0) 
    
    generation = 0
    while env.mario.world == (1, 1):
        print("========================================")
        print("Generation: ", generation)
        plotDataGenerations.append(generation)
        marioNumberArrayPlot = []
        marioPositionPlotData = []
        for p in range(10): # 5 agents for each gen
            # print("Mario: ", p)
            fitness = 0
            currMario = intitialPopualation[p]
            state_size = env.state_size
            state = env.reset()
            state = np.reshape(state, [1, state_size])
            actions = currMario.get_actions()
            actNum = 0
            for act in actions:
                try:
                    filteredMario = [x for x in list(state[0]) if ((x < 82) or (x > 98 and x < 110) or (x > 111 and x < 122) )]
                    index_mario = list(state[0]).index(filteredMario[0])
                    feet_val = state[0][index_mario + 20]
                    # 32 33
                    # 48 49 this is mushroom mario this is also fire flower mario
                    # 64 65
                    # 66 67 this is ducked mushroom mario
                except:
                    fitness = env.mario._level_progress_max
                    # print("mario not found")
                    # print(np.asarray(env.mario.game_area()))
                    # print(fitness)
                    # print('dead')
                    break  
                env.step(act)
                state = np.asarray(env.mario.game_area())
                state = np.reshape(state, [1, state_size])
                # ------ Rendering part -----#
                i = 0
                # env.pyboy.tick()
                # print(np.asarray(env.mario.game_area()))
                # print(env.mario.level_progress)
                env.render(i, feet_val, env)
                env.releaseStep(act)
                # env.render(i, feet_val, env)
                # env.pyboy.tick() # for testing # for testing
                actNum += 1
                fitness = env.mario.level_progress
                
            #check if directory exists
            if not os.path.exists("MarioData\Generation " + str(generation)):  
                os.makedirs("MarioData\Generation " + str(generation))
            currMario.saveActions("MarioData\Generation " + str(generation) + "\marioActions" + str(marioNumber) + ".txt") # for testing
            if not os.path.exists("PlotDataOutput\MarioInGenerationPlots"):
                os.makedirs("PlotDataOutput\MarioInGenerationPlots")
            # print("fitness: ", fitness) # for testing
            # print("position: ", env.mario.level_progress) # for testing
            marioNumberArrayPlot.append(marioNumber)
            marioPositionPlotData.append(fitness)
            marioNumber +=1 # for testing
            trials.append([marioNumber, actions, fitness, actNum])# for testing
            parents.setParents(currMario, fitness, actNum)
            # parents.setBestParent(currMario, fitness, actNum)
            state = env.reset()
        
        plt.plot(marioNumberArrayPlot, marioPositionPlotData)
        plt.xlabel("Current Mario")
        plt.ylabel("Position Reached")
        plt.title("Mario Variation in Generation " + str(generation))
        plt.savefig("PlotDataOutput\MarioInGenerationPlots\Generation " + str(generation))
        plt.clf()
        marioPositionPlotData = []
        marioNumberArrayPlot = []
        marioNumber = 0
        parent1, parent2 = parents.getParents()
        intitialPopualation = parents.mutateComputeNextGen(parent1, parent2)
        print(parents.getFitnessScores(), "parent 1 chromosome pos: ", parents.parent1Chromosome, " parent 2 chromosome pos: ", parents.parent2Chromosome)
        plotDataHighestPosition.append(max(parents.getFitnessScores()))
        # print("Best Parent: ", parents.bestParentFitness, "Best Parent Chromosome: ", parents.bestParentChromosome)
        # for trial in trials: # for testing
            # print(trial[0], trial[2], trial[3])
        # allscores.append([parents.bestParentFitness, parents.bestParentChromosome]) # for testing
        # Appending the fitness score and chromosome of the parents to a list.
        allscores.append([parents.parent1Fitness, parents.parent1Chromosome, parents.parent2Fitness, parents.parent2Chromosome]) # for testing
        # parents.resetParents()
        if not os.path.exists("PlotDataOutput\GrowthPerGenerationPlots"):
            os.makedirs("PlotDataOutput\GrowthPerGenerationPlots")
        if generation > 5:
            plt.plot(plotDataGenerations, plotDataHighestPosition)
        plt.xlabel("Generations")
        plt.ylabel("Distance")
        plt.title("Max distance reached in each generation")
        plt.savefig("PlotDataOutput\GrowthPerGenerationPlots\GenerationVsDistancePlot" + str(generation) + ".png")
        plt.clf()
        
        generation += 1
        print(allscores) # for testing
        print("---------------------------------------------")

if __name__ == '__main__':
    main()
