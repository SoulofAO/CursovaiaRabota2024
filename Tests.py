import main
import Factory
import Investor
import GlobalMarket
import ChildGlobalMarkets.GrowthUpMarket as GrowthUpMarket
import ChildGlobalMarkets.GrowthDownMarket as GrowthDownMarket
import ChildGlobalMarkets.WaveMarket as WaveMarket

factory_class = []
investor_class = []


def GenerateFactories(factory_class):
    factories = []
    for factory_pair in factory_class:
        for x in range(factory_pair[0]):
            new_factory = factory_pair[1](factory_pair[1].__name__ + " " + str(x), [])
            factories.append(new_factory)
    return factories


def GenerateInvestors(investor_class):
    investors = []
    for investor_pair in investor_class:
        for x in range(investor_pair[0]):
            new_investor = investor_pair[1](investor_pair[1].__name__ + " " + str(x), [])
            investors.append(new_investor)
    return investors


def BaseTest():
    main_simulation = main.UMainSimulation([Factory.UFactory("TestFactory", []), Factory.UFactory("TestFactoryV2", [])],
                                           [Investor.UInvestor("TestInvestor", []),
                                            Investor.UInvestor("TestInvestor_V2", [])], GlobalMarket.UGlobalMarket())
    main.main_simulation = main_simulation
    main_simulation.LaunchSimulation()


def GrowthUpTest():
    main_simulation = main.UMainSimulation([Factory.UFactory("TestFactory", []), Factory.UFactory("TestFactoryV2", [])],
                                           [Investor.UInvestor("TestInvestor", []),
                                            Investor.UInvestor("TestInvestor_V2", [])],
                                           GrowthUpMarket.UGrowthUpMarket())
    main.main_simulation = main_simulation
    main_simulation.LaunchSimulation()


def GrowthDownTest():
    main_simulation = main.UMainSimulation([Factory.UFactory("TestFactory", []), Factory.UFactory("TestFactoryV2", [])],
                                           [Investor.UInvestor("TestInvestor", []),
                                            Investor.UInvestor("TestInvestor_V2", [])],
                                           GrowthDownMarket.UGrowthDownMarket())
    main.main_simulation = main_simulation
    main_simulation.LaunchSimulation()


def WaveGrowthTest():

    main_simulation = main.UMainSimulation(GenerateFactories([[3,Factory.UFactory]]),
                                           GenerateInvestors([[20,Investor.UInvestor]]),
                                           WaveMarket.UWaveMarket())
    main.main_simulation = main_simulation
    main_simulation.LaunchSimulation()


WaveGrowthTest()
