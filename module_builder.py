from network_module import NetworkModule
from terminal_module import TerminalModule


from random import randint, normalvariate


class ModuleBuilder:

    def __init__(self, configuration):
        self.configuration = configuration
        self.module_pool = []
        for index, frame in enumerate(configuration['terminal_reference']):
            for key in configuration['terminal_keys']:
                self.module_pool.append(TerminalModule(configuration['terminal_reference'],
                                                       index, key))

    def create_module(self):
        # TODO add input length to configuration
        module_size = randint(1, 10)
        module_inputs = [self.module_pool[randint(0, len(self.module_pool) - 1)] for _ in range(module_size)]

        # TODO Grab normal variate inputs from config
        sigma = 1
        u = 1
        weights = [normalvariate(sigma, u) for _ in range(module_size)]

        # TODO Randomly select activation function from configuration
        activation = sum

        return NetworkModule(module_inputs, weights, activation)
