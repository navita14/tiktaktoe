class Square():
    def __init__(self, row, value = ''):
        self.value = value
        row.squares.append(self)

    def __repr__(self):
        return self.value


    @property
    def value(self):
        return self._value 
    
    @value.setter
    def value(self,new_value):
        self._value = new_value


    
    