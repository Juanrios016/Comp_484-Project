import numpy as np
from MarioBrain2 import MarioBrain
from GenerateGeneration import GenerateGeneration
from Enviroment import Environment

def individualEnvBehavior():
    """could be implememnted to run individual emulators at the same time"""
    pass


def main():
    parents = GenerateGeneration()
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
    '''
    mario1.loadActions("gen1.02DArraygeneracion360-mario1ActionsFS945chrom36.txt")
    mario2.loadActions("gen1.02DArraygeneracion360-mario2ActionsFS943chrom35.txt")
    parents.setParents(mario1, 945, 36)
    parents.setParents(mario2, 943, 35)
    parent1, parent2 = parents.getParents()
    intitialPopualation = parents.mutateComputeNextGen(parent1, parent2)
    '''
    env = Environment() # using only one enviroment to run enverything
    env.pyboy.set_emulation_speed(1) 
    for l in range(500): # do 3 gen so far
        print("Generation: ", l)
        for p in range(len(intitialPopualation)): # 5 agents for each gen
            
            currMario = intitialPopualation[p]
            #state_size = env.state_size
            #state = env.reset()s
            #state = np.reshape(state, [1, state_size])
            actions = currMario.get_actions()
            actNum = 1

            for act in actions:

                if env.mario.lives_left<2:
                    break
                '''
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
                  
                
                state = np.asarray(env.mario.game_area())
                state = np.reshape(state, [1, state_size])
                '''
                
                # ------ Rendering part -----#
                env.step(act[0])
                i=0
                while i < 60: # calss pyboy.tick 60 tmes that is equal to one second in real time
                    env.pyboy.tick()
                    i +=1

                env.releaseStep(act[0])
                fitness = (env.mario._level_progress_max)
                actions[actNum][1] = env.mario._level_progress_max
                actNum += 1           

            parents.setParents(currMario, fitness, actNum)
            print("fitness: ", fitness, "chromosome num: ", actNum) # for testing
            marioNumber +=1 # for testing
            state = env.reset()
        parent1, parent2 = parents.getParents()
        intitialPopualation = parents.mutateComputeNextGen()

        # saves parentss from each gen
        parent1.saveActions("generacion"+str(l)+"-mario1ActionsFS"+str(parents.parent1Fitness) + "chrom" + str(parents.parent1Chromosome)  + ".txt") # for testing
        parent2.saveActions("generacion"+str(l)+"-mario2ActionsFS"+str(parents.parent2Fitness) + "chrom" + str(parents.parent2Chromosome)  + ".txt") # for testing
        print(parents.getFitnessScores(), "parent 1 chromosome pos: ", parents.parent1Chromosome, " parent 2 chromosome pos: ", parents.parent2Chromosome) # for testing
        #allscores.append([parents.parent1Fitness, parents.parent1Chromosome, parents.parent2Fitness, parents.parent2Chromosome]) # for testing
        parents.resetParents()
        print("---------------------------------------------")
    #print(allscores) # for testing
    

if __name__ == '__main__':
    main()
