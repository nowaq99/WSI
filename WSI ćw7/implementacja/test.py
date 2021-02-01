# author: Adam Nowakowski
import gym
from q_learning import q_learning, lake_arbiter, basic_arbiter

env = gym.make('FrozenLake8x8-v0')

for j in [2000]:
    sk = 0
    for k in range(20):
        print(k)
        si = 0
        agent = q_learning(env, j, lake_arbiter)
        for i in range(100):
            done = False
            observation = env.reset()
            agent.reset(observation)
            while not done:
                action = agent.do_action()
                next_observation, reward, done, info = env.step(action)
                reward = basic_arbiter(reward, done)
                agent.observe(next_observation, reward)
            if agent.reward:
                si += 1
        sk += si/100
        print(si/100)
    print(j, ':', sk/20)
