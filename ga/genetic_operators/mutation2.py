from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation
from random import random, randint
from ga.genetic_algorithm import GeneticAlgorithm

class Mutation2(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        pos1 = GeneticAlgorithm.rand.randint(0, len(ind.genome) - 1)
        pos2 = GeneticAlgorithm.rand.randint(0, len(ind.genome) - 1)

        while pos1 == pos2:
            pos2 = GeneticAlgorithm.rand.randint(0, len(ind.genome) - 1)
        # Swap the genes at the selected positions
        ind.genome[pos1], ind.genome[pos2] = ind.genome[pos2], ind.genome[pos1]

    def __str__(self):
        return "Mutation 2 (" + f'{self.probability}' + ")"
