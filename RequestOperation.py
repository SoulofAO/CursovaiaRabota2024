import Active
import enum
from typing import Optional

class EOperation(enum.Enum):
    buy = 0
    sold = 1

class RequestActive:
    def __init__(self, active, cost, b_operation):
        self.active : Optional[Active.UActive] = active
        self.cost = cost
        self.b_operation :Optional[EOperation] = b_operation

    def ExecuteReqeust(self):
        pass

