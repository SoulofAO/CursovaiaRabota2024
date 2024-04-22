import GlobalMarket
import math
import random


class UWaveMarket(GlobalMarket.UGlobalMarket):
    def __init__(self, wave_tick_size=2):
        self.wave_tick_size = wave_tick_size

    def GetGrowthTrend(self, tick):
        random.seed(tick)
        return math.sin(tick / self.wave_tick_size + random.uniform(-0.2, 0.2)) * 100
