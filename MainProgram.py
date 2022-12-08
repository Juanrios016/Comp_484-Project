import numpy as np
from MarioBrain import MarioBrain
from GenerateGeneration import GenerateGeneration
from Enviroment import Environment

def individualEnvBehavior():
    """could be implememnted to run individual emulators at the same time"""
    pass



def main():
    parents = GenerateGeneration()
    trials = [] # for testing
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
    #intitialPopualation = [mario1, mario2, mario3, mario4, mario5, mario6, mario7, mario8, mario9, mario10]
    allscores = [] #for testing to se if fitness score improves for each generation

    mario1.loadActions("Gen75-mario1ActionsFC753chrom131.txt")
    parents.setParents(mario1, 753, 131)
    mario2.loadActions("Gen75-mario2ActionsFC691chrom321.txt")
    parents.setParents(mario2, 691, 321)
    parent1, parent2 = parents.getParents()

    intitialPopualation = parents.computeNextGen(parent1, parent2)

    env = Environment() # using only one enviroment to run enverything
    env.pyboy.set_emulation_speed(0) 
    for l in range(250): # do 3 gen so far
        print("Generation: ", l)
        for p in range(10): # 5 agents for each gen
            
            currMario = intitialPopualation[p]
            state_size = env.state_size
            state = env.reset()
            state = np.reshape(state, [1, state_size])
            actions = currMario.get_actions()
            actNum = 1
            lastScore = []
            lastPos = 0

            for act in actions:
                try:
                    filteredMario = [x for x in list(state[0]) if ((x > 10 and x < 82) or (x > 98 and x < 110) or (x > 111 and x < 122) )]
                    index_mario = list(state[0]).index(filteredMario[0])
                    feet_val = state[0][index_mario + 20]
                    # 32 33
                    # 48 49 this is mushroom mario this is also fire flower mario
                    # 64 65
                    # 66 67 this is ducked mushroom mario
                except:
                    break  
                lastScore.append((env.mario.level_progress))
                lastPos = env.mario.level_progress
                state = np.asarray(env.mario.game_area())
                state = np.reshape(state, [1, state_size])
                # ------ Rendering part -----#
                i = 0
                env.step(act)
                env.render(i, feet_val, env)
                env.releaseStep(act)
                env.render(i, feet_val, env)
                #position = env.mario.level_progress # for testing
                #fitness = env.mario.level_progress # for testing
                actNum += 1

            parents.setParents(currMario, lastScore[len(lastScore)-1], actNum)
            #currMario.saveActions("Gen"+str(l)+"-marioActionsFC"+str(lastPos) + ".txt") # for testing
            print("fitness: ", lastScore[len(lastScore)-1], "chromosome num: ", actNum, "position: ", lastPos) # for testing
            marioNumber +=1 # for testing
            trials.append([marioNumber, lastScore[len(lastScore)-1], actNum])# for testing
            state = env.reset()



        parent1, parent2 = parents.getParents()
        intitialPopualation = parents.computeNextGen(parent1, parent2)

        # saves parentss from each gen
        parent1.saveActions("Gen"+str(l)+"-mario1ActionsFC"+str(parents.parent1Fitness) + "chrom" + str(parents.parent1Chromosome) +".txt") # for testing
        parent2.saveActions("Gen"+str(l)+"-mario2ActionsFC"+str(parents.parent2Fitness) + "chrom" + str(parents.parent2Chromosome) +".txt") # for testing

        print(parents.getFitnessScores(), "parent 1 chromosome pos: ", parents.parent1Chromosome, " parent 2 chromosome pos: ", parents.parent2Chromosome) # for testing
        allscores.append([parents.parent1Fitness, parents.parent1Chromosome, parents.parent2Fitness, parents.parent2Chromosome]) # for testing

        parents.resetParents()
        print("---------------------------------------------")

    #for trial in trials: # for testing
    #        print(trial)
    print(allscores) # for testing
    

if __name__ == '__main__':
    main()
