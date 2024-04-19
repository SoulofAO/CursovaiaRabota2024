import main
import Factory
import Investor
import GlobalMarket
import ChildGlobalMarkets.GrowthUpMarket as GrowthUpMarket


def BaseTest():
    main_simulation = main.UMainSimulation([Factory.UFactory("TestFactory", []), Factory.UFactory("TestFactoryV2", [])],
                                           [Investor.UInvestor("TestInvestor", []),
                                            Investor.UInvestor("TestInvestor_V2", [])], GlobalMarket.UGlobalMarket())
    main.main_simulation = main_simulation
    main_simulation.LaunchSimulation()


def GrowthTest():
    main_simulation = main.UMainSimulation([Factory.UFactory("TestFactory", []), Factory.UFactory("TestFactoryV2", [])],
                                           [Investor.UInvestor("TestInvestor", []),
                                            Investor.UInvestor("TestInvestor_V2", [])], GrowthUpMarket.UGrowthUpMarket())
    main.main_simulation = main_simulation
    main_simulation.LaunchSimulation()


GrowthTest()
