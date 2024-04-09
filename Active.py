from typing import Optional
import Factory
import Investor

class UActive:
    def __init__(self, factory, percent: float, investor):
        self.factory: Optional[Factory.UFactory] = factory
        self.percent = percent
        self.investor: Optional[Investor.UInvestor] = investor

    def GetCost(self):
        return self.percent * self.factory.cost

    def PrintInfo(self):
        print("factory", self.factory, "percent", self.percent, "investor", self.investor)
