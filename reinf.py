import numpy as np
import random

Q = np.zeros((4,4)) 

alpha = 0.1
gamma = 0.9
epsilon = 0.2

def get_reward(state):
    if state == 3:
        return 1
    return 0

def get_next_data(state,action):
    if action == 3 and state <3:
        return state + 1
    elif action == 1 and state <2:
        return state + 2
    return state

for epsilon in range(1000):
    state = 0
    while state != 3:
        if random.uniform((0,1) < epsilon):
            action = random.randint(0,3)
        else:
            action = np.argmax(Q[state])
        next_state = get_next_state(state,action)
        reward = get_reward(next_state)

    Q[state,action] = a[state,action]+ alpha*(reward + gamma*np.max(Q[next_state]) - Q[state,action])

    state = next_state
print("Q-table:")
print(Q)
