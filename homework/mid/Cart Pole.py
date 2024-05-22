import gymnasium as gym
import numpy as np
import math
env = gym.make("CartPole-v1") # 若改用這個，會畫圖

alpha = 0.5          # 學習速率
gamma = 0.9         # 折扣因子
num_episodes = 1000  # 迭代次數
epsilon = 0.8
DISCRETIZE = (1, 1, 6, 3)
q_table = np.zeros(DISCRETIZE + (env.action_space.n,)).astype(int)
boundary = list(zip(env.observation_space.low, env.observation_space.high))
boundary[1] = [-0.5, 0.5]
boundary[3] = [-math.radians(50), math.radians(50)]

def get_state(state, DISCRETIZE, boundary):#離散化
    next_state = [0] * len(state)
    for i, s in enumerate(state):
        l, u = boundary[i][0], boundary[i][1]
        if s <= l:
            next_state[i] = 0
        elif s >= u:
            next_state[i] = DISCRETIZE[i] - 1
        else:
            next_state[i] = int(((s - l) / (u - l)) * DISCRETIZE[i])
    return tuple(next_state)

def choose_action(state, q_table, action_space, epsilon, i):#greed-epsilon
    get_epsilon = lambda i: max(0.01, min(1, 1.0 - math.log10((i+1)/25)))
    if np.random.random_sample() < get_epsilon(i):
        return action_space.sample() 
    else:
        return np.argmax(q_table[state] + np.random.randn(1,env.action_space.n)*(1./(i+1)))

scores = []
for i in range(num_episodes): # 學習循環
    state, info = env.reset() # 初始化環境
    state = get_state(state, DISCRETIZE, boundary)
    rewards = 0
    for j in range(500):
        action = choose_action(state, q_table, env.action_space, epsilon, i)
        next_state, reward, terminated, truncated, info = env.step(action)
        next_state = get_state(next_state, DISCRETIZE, boundary)
        q_table[state + (action,)] += alpha * (reward + gamma * np.amax(q_table[next_state]) - q_table[state + (action,)])
        state = next_state
        rewards += reward
        if terminated:
            break
    scores.append(rewards)
env.close()
print(scores)
print(max(scores),sum(scores)/len(scores))

env = gym.make('CartPole-v1', render_mode="human")

for _ in range(5):
    state, info = env.reset()
    state = get_state(state, DISCRETIZE, boundary)
    for i in range(100):
        env.render()
        action = np.argmax(q_table[state])
        next_state, reward, terminated, truncated, info = env.step(action)
        s, reward, terminated, truncated, info = env.step(action)
        if terminated:
            break
env.close()