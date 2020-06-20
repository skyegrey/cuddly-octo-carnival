class NetworkModule():

    def __init__(self, module_inputs, weights, activation):
        self.module_inputs = module_inputs
        self.weights = weights
        self.activation = activation

    def calculate(self):
        return self.activation(module_input.calculate() * weight for module_input, weight in
                               zip(self.module_inputs, self.weights))

    def __repr__(self):
        representation = ['Module:']

        representation.append(f'Inputs: {self.module_inputs}')
        representation.append(f'Weights: {self.weights}')
        representation.append(f'Activation: {self.activation}')

        return '\n'.join(representation)
