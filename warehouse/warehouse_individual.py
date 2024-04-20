import copy

import numpy as np

from ga.individual_int_vector import IntVectorIndividual
from warehouse.pair import Pair


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblemGA", num_genes: int):
        super().__init__(problem, num_genes)
        self.num_steps = None
        self.forklifts_path = None  # lista de listas, com os caminhos de cada forklift
        # self.forklifts_path = np.empty(len(self.problem.forklifts), dtype=object)
        # self.forklifts_path.fill(np.array([]))

    def compute_fitness(self) -> float:
        # TODO
        self.forklifts_path = [[] for _ in range(len(self.problem.forklifts))]
        # data set um tem de dar 14
        self.num_steps = 0
        j = 0  # numero do forklift
        prodant = 0  # numero do produto anterior no genoma, 0 < qualquer produto no genoma
        self.fitness = 0
        # ultimPosExit=False
        self.genomes_forklifts = [[] for _ in range(len(self.problem.forklifts))]
        # genomes_forklifts = np.empty(len(self.problem.forklifts), dtype=object)
        # genomes_forklifts.fill(np.array([]))

        for prod in self.genome:  # percorrer o genoma
            if prod > len(self.problem.products):
                j += 1
            else:
                self.genomes_forklifts[j] = np.append(self.genomes_forklifts[j],
                                                      prod)  # adicionar o produto ao genoma do forklift

        j = 0
        for genome in self.genomes_forklifts:
            num_steps_forklift = 0
            cellorigem = self.problem.forklifts[j]
            prodant = 0
            for gene in genome:  # percorrer o genoma
                celldestino = self.problem.products[int(gene) - 1]

                if int(gene) < prodant:  # se o produto for menor que o anterior, entao o par é invertido
                    obtainedPair = Pair(celldestino, cellorigem)
                    inverted = True
                else:
                    obtainedPair = Pair(cellorigem, celldestino)
                    inverted = False

                if obtainedPair.hash() in self.problem.agent_search.pairs:  # percorrer lista de pares
                    pair = self.problem.agent_search.pairs[obtainedPair.hash()]
                    if inverted:  # se o par for invertido, entao inverte a lista de celulas visitadas
                        self.forklifts_path[j] = np.append(self.forklifts_path[j], pair.celulas_visitadas[::-1])
                    else:
                        self.forklifts_path[j] = np.append(self.forklifts_path[j], pair.celulas_visitadas)
                    self.fitness += pair.value
                    num_steps_forklift += len(
                        pair.celulas_visitadas)  # incrementar o numero de passos do forklift com o numero de celulas visitadas do par
                cellorigem = celldestino  # preparar a celula de origem para o proximo ciclo
                prodant = int(gene)  # preparar o produto anterior para o proximo ciclo

            celldestino = self.problem.agent_search.exit
            obtainedPair = Pair(cellorigem, celldestino)
            if obtainedPair.hash() in self.problem.agent_search.pairs:  # percorrer lista de pares
                pair = self.problem.agent_search.pairs[obtainedPair.hash()]
                self.fitness += pair.value
                self.forklifts_path[j] = np.append(self.forklifts_path[j], pair.celulas_visitadas)
                num_steps_forklift += len(pair.celulas_visitadas)
                # incrementar o numero de passos do forklift com o numero de celulas visitadas do par
            self.num_steps = max(num_steps_forklift, self.num_steps)
            j += 1
        return self.fitness

    def obtain_all_path(self):
        # TODO
        # Devolver lista de listas, com os caminhos de cada
        return self.forklifts_path, self.num_steps  # num max de pacos que um forklift deu

    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += str(self.genome) + "\n\n"
        # string += str(self.forklifts_path) + "\n\n"
        # TODO
        return string

    def better_than(self, other: "WarehouseIndividual") -> bool:
        return True if self.fitness < other.fitness else False

    # __deepcopy__ is implemented here so that all individuals share the same problem instance
    def __deepcopy__(self, memo):
        new_instance = self.__class__(self.problem, self.num_genes)
        new_instance.genome = self.genome.copy()
        new_instance.fitness = self.fitness
        new_instance.forklifts_path = self.forklifts_path.copy()
        new_instance.num_steps = self.num_steps
        new_instance.genomes_forklifts = self.genomes_forklifts.copy()
        # TODO
        return new_instance
