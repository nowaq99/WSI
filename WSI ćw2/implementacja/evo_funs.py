# author: Adam Nowakowski
"""Module with ancillary functions"""

import random
import numpy as np


def pop_init(pop_size, dim, mu, sigma, seed=None):      # works
    """
    Population initialization function.

    :param pop_size:    population size
    :param dim:         problem dimension
    :param mu:          normal distribution mu parameter
    :param sigma:       normal distribution sigma parameter
    :param seed:        parameter to repeat the experiment

    :return:            list of individuals
    """

    population = list()
    random.seed(seed)
    for i in range(pop_size):
        individual = np.array([[random.normalvariate(mu, sigma)] for j in range(dim)])
        population.append(individual)
    random.seed()
    return population


def evaluate(population, function, resources, maximise):
    """
    Function to evaluate individuals and count average.

    :param function:    objective function
    :param population:  population - list of individuals
    :param resources:   number of function calls
    :param maximise:            flag for identifying is it maximise or not

    :return:            list of evaluations from 0 to 1
    """

    results = list()
    s = 0
    for individual in population:
        result = float(function(individual))
        s = s + result
        if not maximise:
            result = -result
        results.append(result)
        resources[0] = resources[0] + 1
    average = s / len(results)

    return results, average


def tournament_select(population, evaluations, t_size=2, seed=None):
    """
    Tournament select implementation

    :param population:  list of individuals to choose from
    :param evaluations: list of evaluations for each individual
    :param t_size:      number of individuals participating in the tournament
    :param seed:        parameter to repeat the experiment

    :return:            list of selected individuals
    """

    if seed is not None:
        seed = seed + 1
    random.seed(seed)
    selected = list()
    for i in population:
        tournament = [random.randint(0, len(population)-1) for j in range(t_size)]
        t_evaluations = [evaluations[j] for j in tournament]
        winner = population[tournament[t_evaluations.index(max(t_evaluations))]]
        selected.append(winner)
    random.seed()
    return selected


def mutate(population, sigma, seed=None):
    """
    Mutation implementation

    :param population:  list of individuals to mutate
    :param sigma:       mutate parameter N(0, sigma)
    :param seed:        parameter to repeat the experiment

    :return:            individuals after mutation
    """

    if seed is not None:
        seed = seed + 2
    random.seed(seed)
    mutants = list()
    for individual in population:
        mutant = np.array([[float(dim)+random.normalvariate(0, sigma)] for dim in individual])
        mutants.append(mutant)
    random.seed()
    return mutants


def elite_succession(population, population_ev, mutants, mutants_ev, k):
    """
    Elite succession implementation

    :param population:      list of individuals before mutation
    :param population_ev:   list of evaluations for each individual before mutation
    :param mutants:         list of individuals after mutation
    :param mutants_ev:      list of evaluations for each individual after mutation
    :param k:               elite succession parameter

    :return:                list of survivors
    """

    selected = list()
    best = sorted(list(zip(population_ev, population)))[-k:]
    for b in best:
        selected.append(b[1])
    mut = sorted(list(zip(mutants_ev, mutants)))[k:]
    for m in mut:
        selected.append(m[1])
    return selected
