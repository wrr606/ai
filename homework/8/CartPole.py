import gymnasium as gym
env = gym.make("CartPole-v1", render_mode="human") # 若改用這個，會畫圖
# env = gym.make("CartPole-v1", render_mode="rgb_array")
observation, info = env.reset()

action = 1
score = 0
cnt = 0
ans = []

while cnt < 10:
    env.render()
    observation, reward, terminated, truncated, info = env.step(action)
    action = 0 if observation[2]*observation[3]<=0 else 1
    score+=reward
    print('observation=', observation)
    if terminated or truncated: # 這裡要加入程式，紀錄你每次撐多久
        with open('Readme.md', 'a+') as file:
            file.write(f'scores: {score}\n')
        ans.append(score)
        observation, info = env.reset()
        print(f'dead,score:{score}')
        score=0
        cnt+=1

env.close()
with open('Readme.md', 'a+') as file:
    file.write(f'max: {max(ans)}\n')
    file.write(f'min: {min(ans)}\n')
    file.write(f'avg: {sum(ans)/len(ans)}\n')