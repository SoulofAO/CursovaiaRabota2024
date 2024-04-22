import main
import Active
import Trader
import random
from typing import List
from typing import Optional


class UFactory:

    def __init__(self, name, actives, budget=100, normalize_budget=50, cost=100, tick_rate=2, risk=0.01,
                 earn_from_cost_multiplier=0.05, earn_from_budget_multiplier=0.02,
                 sold_to_normalize_budget_multiplier=0.2):
        self.name = name
        self.budget = budget
        self.cost = cost
        self.tick_rate = tick_rate

        self.rating = 1.0
        self.expected_earn = 1.0
        self.risk = risk
        self.pay_dept = 10.0

        self.earn_from_cost_multiplier = earn_from_cost_multiplier
        self.normalize_budget = normalize_budget
        self.earn_from_budget_multiplier = earn_from_budget_multiplier
        self.sold_to_normalize_budget_multiplier = sold_to_normalize_budget_multiplier
        self.tick_index = 0

        self.start_percent_active = 0.5
        self.percent_per_active = 0.1
        self.actives: List[Active.UActive] = actives
        self.trader: Optional[Trader.UTrader] = None

        self.history = []
        self.SaveStateInHistory()

    def PrintInfo(self):
        print("budget", self.budget, "cost", self.cost)

    def SaveStateInHistory(self):
        self.history.append([self.cost])

    def UpdateTickDelayFunction(self):
        self.CalculateNewBudget()
        self.RandomUpdateBudget()
        self.NormalizeBudget()

    def UpdateFunction(self):
        self.SaveStateInHistory()

    def CalculateNewBudget(self):
        self.budget = self.budget + self.cost * self.earn_from_cost_multiplier *(1+main.main_simulation.global_market.GetGrowthTrend(main.main_simulation.tick)) * random.uniform(1-self.risk, 1+self.risk)

    def RandomUpdateBudget(self):
        self.budget = self.budget + random.uniform(-1*self.pay_dept+self.risk, self.pay_dept+self.risk)

    def NormalizeBudget(self):
        if self.budget > self.normalize_budget:
            self.cost = self.cost + (self.budget - self.normalize_budget) * self.earn_from_budget_multiplier
            self.budget = self.normalize_budget
        else:
            sold_value_cost = self.normalize_budget - self.budget
            if self.cost/self.sold_to_normalize_budget_multiplier > sold_value_cost:
                self.budget = self.normalize_budget
                self.cost = self.cost - sold_value_cost*self.sold_to_normalize_budget_multiplier
            else:
                self.Banckrot()

    def Banckrot(self):
        print("factory", self.name, "BANCKROT")
        main.main_simulation.factories.remove(self)
        main.main_simulation.update_entities.remove(self)
        self.actives = []
        for active in self.trader.actives:
            if active.investor is not None:
                active.investor.actives.remove(active)
            main.main_simulation.actives.remove(active)
        self.trader.actives = []
        main.main_simulation.traders.remove(self.trader)
        main.main_simulation.update_entities.remove(self.trader)




    def GenerateActive(self):
        self.trader = Trader.UTrader(self)
        main.main_simulation.AddTrader(self.trader)
        for x in range(int(self.start_percent_active / self.percent_per_active)):
            new_active = Active.UActive(self, self.percent_per_active, None)
            main.main_simulation.actives.append(new_active)
            self.trader.actives.append(new_active)
            self.actives.append(new_active)
