import Factory
import main
import Active
import RequestOperation
from typing import List
import StaticFunctions
import random
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
        self.requests: List[RequestOperation.URequestOperation] = []

    def UpdateTickDelayFunction(self):
        self.UpdateChangeAction()

    def UpdateFunction(self):
        pass

    def PrintInfo(self):
        print("Name", self.name, "budget", self.budget)

    def GetValidActives(self, free_actives):
        free_actives: List[Active.UActive]
        valid_free_actives = []
        for free_active in free_actives:
            if free_active.factory.trader.CostByActive(free_active) < self.budget and abs(
                    free_active.factory.trader.CostByActive(free_active) - free_active.GetRealCost()) < 12:
                valid_free_actives.append(free_active)
        return valid_free_actives

    def UpdateChangeAction(self):
        map_factory_by_interesting = self.GetInterestingFactories()
        for factory_by_interesting in map_factory_by_interesting:
            free_actives = StaticFunctions.GetFreeActives(factory_by_interesting[1].actives)
            if len(free_actives) > 0:
                free_valid_actives = self.GetValidActives(free_actives)
                if len(free_valid_actives) > 0:
                    active_cost = factory_by_interesting[1].trader.CostByActive(free_valid_actives[0])
                    active_cost = active_cost + random.uniform(-0.1,0.1)
                    self.BuyCompanyActive(free_valid_actives[0], active_cost)
                break
        map_factory_by_interesting.reverse()
        reverse_map_factory_by_interesting =  map_factory_by_interesting
        for factory_by_interesting in reverse_map_factory_by_interesting:
            if factory_by_interesting[0]>=0:
                break
            actives_to_sold = self.GetActivesByFactory(factory_by_interesting[1])
            if(len(actives_to_sold)<=0):
                continue
            active_cost = factory_by_interesting[1].trader.CostByActive(actives_to_sold[0])
            active_cost = active_cost + random.uniform(-0.1, 0.1)
            self.SoldCompanyActive(actives_to_sold[0], active_cost)

    def GetInterestingFactories(self):
        map_factory_by_rise = []
        for factory in main.main_simulation.factories:
            factory:Optional[Factory.UFactory]
            if len(factory.history) > factory.tick_rate:
                rise = factory.history[len(factory.history) - 1][0] - factory.history[
                    len(factory.history) - factory.tick_rate][0]
                map_factory_by_rise.append([rise, factory])
        res = sorted(map_factory_by_rise, reverse=True, key=lambda x: x[0])
        return res

    def BuyCompanyActive(self, new_active, cost):
        new_active: Optional[Active.UActive]

        new_request_operation = RequestOperation.URequestOperation(new_active, self, cost,
                                                                   RequestOperation.EOperation.buy)
        new_active.factory.trader.request_operations.append(new_request_operation)
        self.requests.append(new_request_operation)
        self.budget = self.budget - cost

    def SoldCompanyActive(self, remove_active, cost):
        remove_active: Optional[Active.UActive]
        active_cost = remove_active.factory.trader.CostByActive(remove_active)
        remove_request_operation = RequestOperation.URequestOperation(remove_active, self, active_cost,
                                                                      RequestOperation.EOperation.sold)
        remove_active.factory.trader.request_operations.append(remove_request_operation)

    def GetActivesByFactory(self, factory):
        answer_actives = []
        for active in self.actives:
            if active.factory == factory:
                answer_actives.append(active)
        return answer_actives
