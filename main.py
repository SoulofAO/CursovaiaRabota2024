import Factory
import Investor

from typing import Optional
from typing import List
import StaticFunctions

class UMainSimulation:
    def __init__(self):
        self.factories = [Factory.UFactory("TestFactory", [])]
        self.investors = [Investor.UInvestor("TestInvestor", [])]
        self.update_entities = self.factories + self.investors
        self.actives = []

        self.max_hour_num = 100

    def LaunchSimulation(self):
        for factory in self.factories:
            factory.GenerateActive()
        for i in range(self.max_hour_num):
            print("Day",i)
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
        print("")




main_simulation = None