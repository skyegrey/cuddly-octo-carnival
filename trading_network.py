class TradingNetwork:

    def __init__(self, output_module):
        self.output_module = output_module

    def get_network_value(self):
        return self.output_module.calculate()
