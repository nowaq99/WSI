# author: Adam Nowakowski

import evolution as ev
import functions as funs


seeds = [342, 12312, 1, 12333, 900, 112, 997, 111111]

p_size = 500
mutation_sigma = 0.08
elite_succession = 300
tournament_size = 2
mu1 = 0
mu2 = 3
sigma1 = 1
sigma2 = 1
function1 = funs.f1
function2 = funs.f2
bud1 = 10**5
bud2 = 10**5

for seed in seeds:
    evo = ev.EvolutionaryMethod(p_size, mutation_sigma, elite_succession, tournament_size, mu2, sigma2)
    out = evo.minimise(function2, 2, bud2, seed)
    print(out)
