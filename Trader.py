import Active
import RequestOperation
import StaticFunctions
import Factory
from typing import List
from typing import Optional


class UTrader:
    def __init__(self, factory, tick_rate = 1):
        self.actives: List[Active.UActive] = []
        self.request_operations: List[RequestOperation.URequestOperation] = []
        self.buy_number_operations = 3
        self.sold_number_operations = 3
        self.tick_rate = tick_rate
        self.tick_index = 0
        self.factory: Optional[Factory.UFactory] = factory

        self.priority = 0

    def UpdateTickDelayFunction(self):
        self.UpdatePriority()
        self.UpdateBuyAndSales()

    def UpdateFunction(self):
        pass

    def UpdatePriority(self):
        buy_request_operations = StaticFunctions.FilterRequestByType(self.request_operations,
                                                                     RequestOperation.EOperation.buy)
        sold_request_operations = StaticFunctions.FilterRequestByType(self.request_operations,
                                                                      RequestOperation.EOperation.sold)
        self.priority = self.priority + len(buy_request_operations) - len(sold_request_operations)

    def UpdateBuyAndSales(self):
        buy_request_operations = StaticFunctions.FilterRequestByType(self.request_operations,
                                                                     RequestOperation.EOperation.buy)
        for k in range(self.buy_number_operations):
            max_cost_request: RequestOperation.URequestOperation = StaticFunctions.GetMaxCostRequest(
                buy_request_operations)
            if max_cost_request is None:
                break
            max_cost_request.ExecuteReqeust()
            buy_request_operations.remove(max_cost_request)

        sold_request_operations = StaticFunctions.FilterRequestByType(self.request_operations,
                                                                      RequestOperation.EOperation.sold)
        for k in range(self.sold_number_operations):
            min_cost_request: RequestOperation.URequestOperation = StaticFunctions.GetMinCostRequest(
                sold_request_operations)
            if min_cost_request is None:
                break
            min_cost_request.ExecuteReqeust()
            sold_request_operations.remove(min_cost_request)

        while len(self.request_operations)>0:
            self.request_operations[0].RejectRequest()

    def CostByActive(self, active):
        active : Optional[Active.UActive]
        return active.GetRealCost() + self.priority

    def PrintInfo(self):
        print("TraderOwnerName", self.factory.name,"Priority", self.priority,"RequestOperationsNumber", len(self.request_operations))
