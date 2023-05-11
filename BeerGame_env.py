import random
import gymnasium as gym
import numpy as np

def getAllPossibleNextAction(self):
    step_matrix = [x != None for x in environment_matrix[self.cur_pos]]
    actions = []
    if(step_matrix[0]):
        actions.append(0) 
    if(step_matrix[1]):
        actions.append(1)
    
    return(gym.spaces.Discrete(len(actions)))

win_loss_states = [0,6]

environment_matrix = [[-1000, 0],
                  [-100, 0],
                  [0, 0],
                  [0, 0],
                  [0, 0],
                  [0, 100],
                  [0, 0],
                  [100, 0],
                  [0, 0],
                  [0, -1000]]

class BeerGame(gym.Env):
    def __init__(self, max_steps=100):
        self.cur_pos = random.choice([x for x in range(0,9)])
        self.action_space = getAllPossibleNextAction(self)
        self.observation_space = self.make_observation_space()
        # self.log = ''
        # self.max_steps = max_steps

    def make_observation_space(self):
        low = 0
        high = 10
        shape = (1,)
        return gym.spaces.Box(low, high, shape, np.int32)
        
    def reset(self):
        self.cur_pos = random.choice([x for x in range(0,9)])
        return (self.cur_pos,)

    def step(self, action):
        if action == 0:
            if self.cur_pos != 0:
                next_pos = self.cur_pos - 1
            else:
                next_pos = self.cur_pos
        elif self.cur_pos != 9:
            next_pos = self.cur_pos + 1
        else:
            next_pos = self.cur_pos
        
        reward = environment_matrix[self.cur_pos][action]

        if reward < 100: reward -= 5 # Penalty for taking more steps
        
        done = self.cur_pos in win_loss_states

        if not done: self.cur_pos = next_pos
        
        return (self.cur_pos,), reward, done, {}
    
    # def close(self):
    #     pass
        
    # def render(self, mode=None):
    #     print(self.log)
    #     self.log = ''
