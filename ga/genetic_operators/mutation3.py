from random import random, randint
from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation
from ga.genetic_algorithm import GeneticAlgorithm

class Mutation3(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        """for i in range(len(ind.genome) - 1, 0, -1):
            j = GeneticAlgorithm.rand.randint(0, i)
            ind.genome[i], ind.genome[j] = ind.genome[j], ind.genome[i]"""
        # Select two random positions in the genome
        pos1 = GeneticAlgorithm.rand.randint(0, len(ind.genome) - 1)
        pos2 = GeneticAlgorithm.rand.randint(0, len(ind.genome) - 1)
        while pos1 == pos2:
            pos2 = GeneticAlgorithm.rand.randint(0, len(ind.genome) - 1)
        # Reverse the order of genes between pos1 and pos2
        ind.genome[pos1:pos2 + 1] = ind.genome[pos1:pos2 + 1][::-1]

    def __str__(self):
        return "Mutation 3 (" + f'{self.probability}' + ")"
