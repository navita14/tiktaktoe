class Square():
    def __init__(self, row, value = "X"):
        self.value = value
        self.row = row
        row.squares.append(self)

    def __repr__(self):
        return self.value


    @property
    def value(self):
        return self._value 
    
    @value.setter
    def value(self,new_value):
        self._value = new_value


    
    