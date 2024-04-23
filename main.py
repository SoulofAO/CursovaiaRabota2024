import Factory
import Investor
import Trader
import GlobalMarket
from typing import Optional
from typing import List
import StaticFunctions
import History


class UMainSimulationHistory(History.UHistory):
    def __init__(self, owner):
        owner: Optional[UMainSimulation]
        super().__init__(owner)
        self.length_bought_action = []
        self.sum_cost_factory = []

    def SaveHistory(self):
        self.length_bought_action.append(len(self.owner.actives) - len(StaticFunctions.GetFreeActives(self.owner.actives)))

        self.sum_cost_factory.append(sum(factory.cost for factory in self.owner.factories))


class UMainSimulation:
    def __init__(self, factories, investors, global_market):
        self.factories: List[Factory.UFactory] = factories
        self.investors: List[Investor.UInvestor] = investors
        self.global_market: Optional[GlobalMarket.UGlobalMarket] = global_market
        self.traders: List[Trader.UTrader] = []

        self.update_entities = []
        self.update_entities = self.update_entities + self.factories
        self.update_entities = self.update_entities + self.investors
        self.actives = []
        self.tick = 0

        self.history : Optional[UMainSimulationHistory] = None

        self.max_hour_num = 30

    def AddTrader(self, trader):
        self.traders.append(trader)
        self.update_entities.append(trader)

    def LaunchSimulation(self):
        self.history = UMainSimulationHistory(self)
        for factory in self.factories:
            factory.GenerateActive()
        for i in range(self.max_hour_num):
            self.tick = i
            print("Day", i)
            self.PrintAllInformation()
            for update_entity in self.update_entities:
                update_entity.UpdateFunction()
                update_entity.tick_index = update_entity.tick_index + 1
                if update_entity.tick_index > update_entity.tick_rate:
                    update_entity.UpdateTickDelayFunction()
                    update_entity.PrintInfo()
                    update_entity.tick_index = 0
            self.history.SaveHistory()

    def PrintAllInformation(self):
        print("Actives")
        for active in self.actives:
            active.PrintInfo()
        print("Investors")
        for investor in self.investors:
            investor.PrintInfo()
        print("Factories")
        for factory in self.factories:
            factory.PrintInfo()
        print("Traders")
        for trader in self.traders:
            trader.PrintInfo()
        print("Market Situation", self.global_market.GetGrowthTrend(self.tick))
        print("")


main_simulation = None
