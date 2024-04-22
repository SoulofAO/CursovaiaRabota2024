import GlobalMarket


class UGrowthDownMarket(GlobalMarket.UGlobalMarket):
    def GetGrowthTrend(self, tick):
        return -20
