import Active
import Investor
import enum
from typing import Optional


class EOperation(enum.Enum):
    buy = 0
    sold = 1


class URequestOperation:
    def __init__(self, active, investor, cost, operation):
        self.active: Optional[Active.UActive] = active
        self.investor: Optional[Investor.UInvestor] = investor
        self.cost = cost
        self.operation: Optional[EOperation] = operation

    def ExecuteReqeust(self):
        self.active.factory.trader.request_operations.remove(self)
        match self.operation:
            case EOperation.buy:
                self.active.factory.budget = self.active.factory.budget + self.cost
                self.investor.actives.append(self.active)
                self.active.investor = self.investor

            case EOperation.sold:
                self.investor.budget = self.investor.budget + self.cost
                self.active.factory.budget = self.active.factory.budget - self.cost
                if self.active in self.investor.actives:
                    self.investor.actives.remove(self.active)
                self.active.investor = None

    def RejectRequest(self):
        self.investor.budget = self.investor.budget + self.cost

        if self in self.investor.requests:
            self.investor.requests.remove(self)
        self.active.factory.trader.request_operations.remove(self)
