# author: Adam Nowakowski
import numpy as np


class Agent:
    def __init__(self, init_state, env_space, action_space):
        self.reward = 0
        self.state = init_state
        self.q_fun = QFunction(env_space, action_space)

    def observe(self, state, reward):
        self.state = state,
        self.reward = self.reward + reward

    def do_action(self):
        action = self.q_fun.best_out(self.state)[1]
        return action

    def training_action(self):
        probabilities = list()
        actions = self.q_fun.table[self.state]
        t = 10
        for action in actions:
            probability = np.exp(action/t)/sum(np.exp(actions/t))
            probabilities.append(probability)
        return np.random.choice(len(probabilities), 1, p=probabilities)[0]

    def reset(self, init_state):
        self.reward = 0
        self.state = init_state


class QFunction:
    def __init__(self, env_space, action_space):
        self.table = np.zeros([env_space, action_space])

    def best_out(self, state):
        max_reward = max(self.table[state])
        best_moves = np.where(self.table[state] == max_reward)[0]
        best_move = np.random.choice(best_moves)
        return max_reward, best_move

    def out(self, state, move):
        return self.table[state][move]


def lake_arbiter(basic_reward, done):
    if basic_reward == 1:
        return 40
    else:
        if done:
            return -100
        else:
            return 1


def basic_arbiter(basic_reward, done):
    return basic_reward


def q_learning(env, iterations, arbiter=basic_arbiter):
    observation = env.reset()
    agent = Agent(observation, env.observation_space.n, env.action_space.n)
    q_fun = agent.q_fun
    table = q_fun.table
    prediction = 20
    discount = 1 - 1/prediction
    beta = 1 - 1/iterations
    done = False
    t = 1
    for k in range(iterations):
        while not done:
            action = agent.training_action()
            next_observation, reward, done, info = env.step(action)
            reward = arbiter(reward, done)
            agent.observe(next_observation, reward)
            table[observation][action] = table[observation][action] + (beta**iterations)*(reward + discount*q_fun.best_out(next_observation)[0] - table[observation][action])
            observation = next_observation
            t = t+1
        done = False
        observation = env.reset()
        agent.reset(observation)
    return agent
