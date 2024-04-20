
from abc import abstractmethod

import numpy as np

from ga.problem import Problem
from ga.individual import Individual

from ga.genetic_algorithm import GeneticAlgorithm
class IntVectorIndividual(Individual):

    def __init__(self, problem: Problem, num_genes: int):
        super().__init__(problem, num_genes)
        # TODO
        #criar genoma e colocar valores entre 1 e num_genes, nao pode haver repetidos
        self.genome = [i for i in range(1, num_genes + 1)]
        GeneticAlgorithm.rand.shuffle(self.genome)
        #tirar o print
        #print(self.genome)

    def swap_genes(self, other, index: int):
        aux = self.genome[index]
        self.genome[index] = other.genome[index]
        other.genome[index] = aux

    @abstractmethod
    def compute_fitness(self) -> float:
        pass

    @abstractmethod
    def better_than(self, other: "IntVectorIndividual") -> bool:
        pass
