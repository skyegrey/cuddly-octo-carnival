from collections import deque
from network_builder import NetworkBuilder
import pygame


def visualize_network(network):
    output_module = network.output_module

    # TODO square width calculation
    square_width = 50

    # TODO Layer calculation
    layers = 2

    # Some other config that could be parameterized
    padding = 50
    layer_width = 50
    # TODO Needs to be calculated dynamically
    layer_height = 750
    background_color = (153, 153, 204)

    # Calculations
    width = 2 * padding + layers * square_width + (layers - 1) * layer_width
    height = layer_height + 2 * padding

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    screen.fill(background_color)

    # Print box for current module
    layer = 1
    modules_on_layer = 1
    layer_module_number = 1

    x_coord = padding + layer * square_width + layer * layer_width
    y_coord = round(padding + layer_height / 2 - (square_width / 2))

    pygame.draw.rect(screen, (51, 255, 255), pygame.Rect(x_coord, y_coord, square_width, square_width))
    pygame.display.update()

    layer = 0
    x_coord = padding + layer * square_width + layer * layer_width
    modules_on_layer = len(output_module.module_inputs)
    print(f'modules on layer: {modules_on_layer}')
    width_gaps = (layer_height - square_width * modules_on_layer) / modules_on_layer
    print(width_gaps)
    for layer_module_number, terminal in enumerate(output_module.module_inputs):
        y_coord = round(padding + width_gaps * layer_module_number + square_width * layer_module_number)
        pygame.draw.rect(screen, (45, 245, 245), pygame.Rect(x_coord, y_coord, square_width, square_width))
        pygame.display.update()

    print(output_module)
    # Run the display until exit
    display = True
    while display:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                display = False
                pygame.quit()


if __name__ == '__main__':
    test_terminals = deque()
    test_terminals.append({
            'ask': 195.5,
            'bid': 200.0
        })

    test_terminals.appendleft({
        'ask': 200.0,
        'bid': 210.0
    })

    network_configuration = {
        'module_configuration': {
            'terminal_reference': test_terminals,
            'terminal_keys': ['ask', 'bid']
        }
    }

    network_builder = NetworkBuilder(network_configuration)
    test_network = network_builder.build_network()

    visualize_network(test_network)