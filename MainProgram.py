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
    intitialPopualation = [mario1, mario2, mario3, mario4, mario5]

    allscores = [] #for testing to se if fitness score improves for each generation

    env = Environment() # using only one enviroment to run enverything
    env.pyboy.set_emulation_speed(0) 

    for l in range(10): # do 3 gen so far
        for p in range(5): # 5 agents for each gen
            
            currMario = intitialPopualation[p]
            state_size = env.state_size
            state = env.reset()
            state = np.reshape(state, [1, state_size])
            actions = currMario.get_actions()

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
                    print("error", np.asarray(env.mario.game_area()))
                    break
                    
                           
                env.step(act)

                state = np.asarray(env.mario.game_area())
                state = np.reshape(state, [1, state_size])
                
                # ------ Rendering part -----#
                i = 0
                # env.pyboy.tick()
                # print(np.asarray(env.mario.game_area()))
                print(env.mario.level_progress)
                env.render(i, feet_val, env)
                env.releaseStep(act)
                env.render(i, feet_val, env)
                # env.pyboy.tick()
                
                position = env.mario._level_progress_max # for testing
                fitness = env.getFitness() # for testing
            
            currMario.saveActions("marioActions" + str(marioNumber) + ".txt") # for testing
            print("fitness: ", env.getFitness()) # for testing
            print("position: ", position) # for testing
            marioNumber +=1 # for testing
            trials.append([marioNumber, actions, fitness])# for testing
            
            parents.setParents(currMario, fitness)
            state = env.reset()



        parent1, parent2 = parents.getParents()
        intitialPopualation = parents.computeNextGen(parent1, parent2)

        print(parents.getFitnessScores()) # for testing
        for trial in trials: # for testing
            print(trial[0], trial[2])
        allscores.append([parents.parent1Fitness, parents.parent2Fitness]) # for testing

        parents.resetParents()

    print(allscores) # for testing

if __name__ == '__main__':
    main()
