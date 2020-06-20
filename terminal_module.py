# Might be too heavy to pass the entire window reference, not sure yet
class TerminalModule:

    def __init__(self, terminal_set, index, key):
        self.terminal_set = terminal_set
        self.index = index
        self.key = key

    def calculate(self):
        return self.terminal_set[self.index][self.key]

    def __repr__(self):
        return f'(Frame {self.index}: {self.key}: {self.terminal_set[self.index][self.key]})'