from typing import List


def GetFreeActives(actives):
    free_actives = []
    for active in actives:
        if active.investor is None:
            free_actives.append(active)
    return free_actives


def GetMaxCostRequest(requests):
    max_cost = -1.0
    max_request = None
    for request in requests:
        if request.cost > max_cost:
            max_cost = request.cost
            max_request = request
    return max_request


def GetMinCostRequest(requests):
    min_cost = 1000000000000
    max_request = None
    for request in requests:
        if request.cost < min_cost:
            min_cost = request.cost
            max_request = request
    return max_request


def FilterRequestByType(requests, l_filter_operation):
    l_result_request = []
    for request in requests:
        if request.operation == l_filter_operation:
            l_result_request.append(request)
    return l_result_request


def GetFactoryName(factory):
    if factory is None:
        return "None"
    else:
        return factory.name


def GetInvestorName(investor):
    if investor is None:
        return "None"
    else:
        return investor.name
