import numpy as np
import random

Q = np.zeros((4, 4)) 

alpha = 0.1
gamma = 0.9
epsilon = 0.2 

def get_reward(state):
    return 1 if state == 3 else 0

def get_next_state(state, action):
   
    if action == 3 and state < 3:
        return state + 1
    elif action == 1 and state < 2:
        return state + 2
    return state
for episode in range(1000):
    state = 0
    while state != 3:
        if random.random() < epsilon:
            action = random.randint(0, 3)
        else:
            action = np.argmax(Q[state])
            
        next_state = get_next_state(state, action)
        reward = get_reward(next_state)

        Q[state, action] = Q[state, action] + alpha * (reward + gamma * np.max(Q[next_state]) - Q[state, action])

        state = next_state

print("Q-table:")
print(Q)

