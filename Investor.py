import main
import Active
from typing import List
import StaticFunctions
from typing import Optional


class UInvestor:
    # tick_rate per hour
    def __init__(self, name, actives, budget=100, tick_rate=1, max_investing_factory=5):
        self.name = name
        self.budget = budget
        self.actives: List[Active.UActive] = actives
        self.tick_rate = tick_rate
        self.tick_index = 0
        self.max_investing_factory = max_investing_factory

    def UpdateTickDelayFunction(self):
        map_factory_by_interesting = self.GetInterestingFactories()
        for factory_by_interesting in map_factory_by_interesting:
            free_actives = StaticFunctions.GetFreeActives(factory_by_interesting[1].actives)
            if len(free_actives) > 0:
                free_valid_actives = self.GetValidActive(free_actives)
                if len(free_valid_actives)>0:
                    self.BuyCompanyActive(free_valid_actives[0])
                return

    def UpdateFunction(self):
        pass

    def PrintInfo(self):
        print("budget", self.budget)

    def GetValidActive(self, free_actives):
        free_actives: List[Active.UActive]
        valid_free_actives = []
        for free_active in free_actives:
            if free_active.GetCost() < self.budget:
                valid_free_actives.append(free_active)
        return valid_free_actives

    def GetInterestingFactories(self):
        map_factory_by_rise = []
        for factory in main.main_simulation.factories:
            if len(factory.history)>2:
                rise = factory.history[len(factory.history) - 1][0] - factory.history[
                    len(factory.history) - 2][0]
                map_factory_by_rise.append([rise, factory])
        res = sorted(map_factory_by_rise, reverse=True, key=lambda x: x[0])
        return res

    def BuyCompanyActive(self, new_active):
        new_active: Optional[Active.UActive]
        self.budget = self.budget - new_active.GetCost()
        self.actives.append(new_active)
        new_active.factory.budget = new_active.factory.budget+new_active.GetCost()
        new_active.investor = self

    def SoldCompanyActive(self, remove_active):
        remove_active: Optional[Active.UActive]
        self.budget = self.budget + remove_active.GetCost()
        self.actives.append(remove_active)
        remove_active.factory.budget = remove_active.factory.budget + remove_active.GetCost()
        remove_active.investor = self
