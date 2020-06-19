class Module:

    def __init__(self, module_inputs, weights, activation):
        self.module_inputs = module_inputs
        self.weights = weights
        self.activation = activation

    def calculate(self):
        return self.activation(module_input * weight for module_input, weight in zip(self.module_inputs, self.weights))
