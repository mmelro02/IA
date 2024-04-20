from ga.genetic_operators.recombination import Recombination
from ga.individual import Individual
from ga.genetic_algorithm import GeneticAlgorithm

class Recombination3(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        len_genoma = len(ind1.genome)
        cycle = [False] * len_genoma  # Keeps track of which positions have been filled
        offspring1 = [-1] * len(ind1.genome) # -1 means that the position hasn't been filled yet
        offspring2 = offspring1

        # Create the first cycle
        cycle_start = ind1.genome[0]  # Start the cycle with the first gene of the first parent
        cycle_position = 0
        while not cycle[cycle_position]:
            cycle[cycle_position] = True  # Mark the position as filled
            offspring1[cycle_position] = ind1.genome[cycle_position]  # Copy the gene from the first parent
            offspring2[cycle_position] = ind2.genome[cycle_position]  # Copy the gene from the second parent
            cycle_position = ind1.genome.index(ind2.genome[cycle_position])  # Find the position of the gene from the
            # 2nd parent in the 1st parent

        # Fill in the remaining positions using the corresponding genes from the other parent
        for i in range(len_genoma):
            if offspring1[i] == -1: # If the position hasn't been filled yet
                offspring1[i] = ind2.genome[i] # Copy the gene from the second parent
            if offspring2[i] == -1:
                offspring2[i] = ind1.genome[i] # Copy the gene from the first parent

        # Update the genomes of the individuals with the new offspring
        ind1.genome[:] = offspring1
        ind2.genome[:] = offspring2

    def __str__(self):
        return "Recombination 3 (" + f'{self.probability}' + ")"