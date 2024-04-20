from ga.individual import Individual
from ga.genetic_operators.recombination import Recombination
from random import random, randint
from ga.genetic_algorithm import GeneticAlgorithm


class Recombination2(Recombination):

    def init(self, probability: float):
        super().init(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        # Select two random crossover points
        cut1 = GeneticAlgorithm.rand.randint(0, len(ind1.genome) - 1)
        cut2 = GeneticAlgorithm.rand.randint(0, len(ind1.genome) - 1)

        if cut2 < cut1:
            cut1, cut2 = cut2, cut1

        # Copy the segment between the crossover points from ind1 to offspring1
        offspring1 = ind1.genome[cut1:cut2 + 1]

        remaining_genes = set(gene for gene in ind2.genome if gene not in offspring1)

        index = 0
        for i in range(len(offspring1)):
            if offspring1[i] in remaining_genes:
                offspring1[i] = remaining_genes.pop()
                index += 1

        # Create offspring2 by swapping parents
        offspring2 = ind2.genome[cut1:cut2 + 1]

        remaining_genes = set(gene for gene in ind1.genome if gene not in offspring2)
        index = 0
        for i in range(len(offspring2)):
            if offspring2[i] in remaining_genes:
                offspring2[i] = remaining_genes.pop()
                index += 1

        # Update the genomes of the individuals with the new offspring
        ind1.genome[cut1:cut2 + 1] = offspring1
        ind2.genome[cut1:cut2 + 1] = offspring2

    def str(self):
        return "Recombination 2 (" + f'{self.probability}' + ")"