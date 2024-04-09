from typing import List


def GetFreeActives(actives):
    free_actives = []
    for active in actives:
        if active.investor is None:
            free_actives.append(active)
    return free_actives
