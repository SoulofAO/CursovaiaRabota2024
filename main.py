import Factory
import Investor
import Trader

from typing import Optional
from typing import List
import StaticFunctions


class UMainSimulation:
    def __init__(self):
        self.factories: List[Factory.UFactory] = [Factory.UFactory("TestFactory", []), Factory.UFactory("TestFactoryV2", [])]
        self.investors: List[Investor.UInvestor] = [Investor.UInvestor("TestInvestor", []), Investor.UInvestor("TestInvestor_V2", [])]
        self.traders: List[Trader.UTrader] = []

        self.update_entities = []
        self.update_entities = self.update_entities + self.factories
        self.update_entities = self.update_entities + self.investors
        self.actives = []

        self.max_hour_num = 10

    def AddTrader(self, trader):
        self.traders.append(trader)
        self.update_entities.append(trader)

    def LaunchSimulation(self):
        for factory in self.factories:
            factory.GenerateActive()
        for i in range(self.max_hour_num):
            print("Day", i)
            self.PrintAllInformation()
            for update_entity in self.update_entities:
                update_entity.UpdateFunction()
                update_entity.tick_index = update_entity.tick_index + 1
                if update_entity.tick_index > update_entity.tick_rate:
                    update_entity.UpdateTickDelayFunction()
                    update_entity.PrintInfo()
                    update_entity.tick_index = 0

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
        print("")



main_simulation = None
