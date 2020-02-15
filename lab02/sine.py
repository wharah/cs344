"""
This module implements local search on a sine function variant.

@author: smw42
@version 14feb2020
"""
import math
import time
from search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange


class SineVariant(Problem):
    """
    State: x value for the abs function variant f(x)
    Move: a new x value delta steps from the current x (in both directions)
    """

    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta

    def actions(self, state):
        return [state + self.delta, state - self.delta]

    def result(self, stateIgnored, x):
        return x

    def value(self, x):
        return math.fabs(x * math.sin(x))


if __name__ == '__main__':
    # Formulate a problem with a 2D hill function and a single maximum value.

    maxHill = 0
    maxSim = 0
    totalHill = 0
    totalSim = 0

    restarts = 100
    maximum = 30
    for iteration in range(0, restarts):
        # Formulate a problem with a 2D hill function and a single maximum value.
        initial = randrange(0, maximum)
        p = SineVariant(initial, delta=1.0)

        # Solve the problem using hill-climbing.
        hill_solution = hill_climbing(p)
        totalHill += p.value(hill_solution)
        # Check if we found a better hill-climbing solution.
        if p.value(hill_solution) > p.value(maxHill):
            hill_solution_max = hill_solution

        # Solve the problem using simulated annealing.
        annealing_solution = simulated_annealing(
            p,
            exp_schedule(k=20, lam=0.005, limit=1000)
        )
        totalSim += p.value(annealing_solution)
        # Check if we found a better simulated annealing solution.
        if p.value(annealing_solution) > p.value(maxSim):
            annealing_solution_max = annealing_solution

    print('Initial                      x: ' + str(p.initial)
          + '\t\tvalue: ' + str(p.value(initial))
          )
    print('Hill-climbing solution       x: ' + str(maxHill)
          + '\tvalue: ' + str(p.value(maxHill))
          )
    print('Simulated annealing solution x: ' + str(maxSim)
          + '\tvalue: ' + str(p.value(maxSim))
          )
    print('Hill-climbing average: ' + str(totalHill / restarts))
    print('Simulated annealing average: ' + str(totalSim / restarts))
