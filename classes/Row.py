class Row():
    def __init__(self, index = 0):
        self.squares = []

    def enter_value(self, square, value):
        square.value = value
