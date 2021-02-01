# author: Adam Nowakowski
"""Module with evolutionary algorithm implementation"""

import evo_funs
import functions
import matplotlib.pyplot as plt


class EvolutionaryMethod:

    def __init__(self, pop_size, mutation, elite_succession, tournament_size, mu, sigma):
        """
        Parameter initialization

        :param pop_size:            population size
        :param mutation:            mutation sigma parameter
        :param elite_succession:    elite succession k parameter
        :param tournament_size:     number of individuals participating in the tournament
        :param mu:                  initial population parameter in N(mu, sigma)
        :param sigma:               initial population parameter in N(mu, sigma)
        """

        self.pop_size = pop_size
        self.mutation = mutation
        self.elite_succession = elite_succession
        self.tournament_size = tournament_size
        self.mu = mu
        self.sigma = sigma

    def maximise(self, fun, dim, budget, seed=None, maximise=True):
        """
        Algorithm implementation

        :param fun:                 function to maximise
        :param dim:                 number of function dimensions
        :param budget:              number of function calls
        :param seed:                parameter to repeat the experiment
        :param maximise:            flag for identifying is it maximise or not

        :return:                    average value of last individuals
        """

        iteration = 0
        resources = [0]
        average_results = list()
        population = evo_funs.pop_init(self.pop_size, dim, self.mu, self.sigma, seed)
        population_ev, average = evo_funs.evaluate(population, fun, resources, maximise)
        average_results.append(average)
        while resources[0] < budget:
            if seed is not None:
                seed = seed + 5
            selected = evo_funs.tournament_select(population, population_ev, self.tournament_size)
            mutants = evo_funs.mutate(selected, self.mutation, seed)
            mutants_ev = evo_funs.evaluate(mutants, fun, resources, maximise)[0]
            population = evo_funs.elite_succession(population, population_ev, mutants, mutants_ev, self.elite_succession)
            population_ev, average = evo_funs.evaluate(population, fun, resources, maximise)
            average_results.append(average)
            # print(f"iteracja: {iteration}")
            # print(f"wywołania: {resources[0]}")
            # print(f"watrość: {average}")
            iteration = iteration + 1
        plt.plot(average_results)
        return average

    def minimise(self, fun, dim, budget, seed=None):

        return self.maximise(fun, dim, budget, seed, False)
