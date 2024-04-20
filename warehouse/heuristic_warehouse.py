from agentsearch.heuristic import Heuristic
from warehouse.warehouse_problemforSearch import WarehouseProblemSearch
from warehouse.warehouse_state import WarehouseState


class HeuristicWarehouse(Heuristic[WarehouseProblemSearch, WarehouseState]):

    def __init__(self):
        super().__init__()

    def compute(self, state: WarehouseState) -> float:
        return abs(state.line_forklift - self._problem.goal_position.line) + abs(state.column_forklift - self._problem.goal_position.column)

    def __str__(self):
        return "# TODO"

