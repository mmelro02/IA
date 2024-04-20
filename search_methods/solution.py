from agentsearch.problem import Problem
from search_methods.node import Node
from warehouse.cell import Cell


class Solution:

    def __init__(self, problem: Problem, goal_node: Node):
        self.problem = problem
        self.goal_node = goal_node
        self.actions = []
        self.celulas_visitadas = []
        node = self.goal_node
        while node.parent is not None:
            self.actions.insert(0, node.state.action)
            cell = Cell(node.state.line_forklift, node.state.column_forklift)
            self.celulas_visitadas.insert(0, cell) # Guardar as celulas visitadas
            node = node.parent
        cell = Cell(node.state.line_forklift, node.state.column_forklift)
        self.celulas_visitadas.insert(0, cell)  # Guardar a ultima celula

    @property
    def cost(self) -> int:
        return self.problem.compute_path_cost(self.actions)
