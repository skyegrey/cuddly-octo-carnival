from module_builder import ModuleBuilder
from trading_network import TradingNetwork
from collections import deque


class NetworkBuilder:

    def __init__(self, configuration):
        self.configuration = configuration
        module_configuration = configuration['module_configuration']
        self.module_builder = ModuleBuilder(module_configuration)

    def build_network(self):
        return TradingNetwork(self.module_builder.create_module())

    def crossover_networks(self):
        pass

    def mutate_network(self):
        pass


if __name__ == '__main__':
    test_terminals = deque()
    test_terminals.append({
            'ask': 195.5,
            'bid': 200.0
        })

    network_configuration = {
        'module_configuration': {
            'terminal_reference': test_terminals,
            'terminal_keys': ['ask', 'bid']
        }
    }

    network_builder = NetworkBuilder(network_configuration)
    test_network = network_builder.build_network()
    print(test_network)

    test_terminals.appendleft({
        'ask': 200.0,
        'bid': 210.0
    })

    print(test_network)
    print(test_network.get_value())