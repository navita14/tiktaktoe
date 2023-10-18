class Row():
    rows = []
    def __init__(self, index):
        self.squares = []
        self.index = index
        Row.rows.append(self)
