from classes.Row import Row
from classes.Square import Square
from classes.Player import Player

#three rows
row = Row()
new_row = Row()

player_1 = Player("Nav")

#row 1 square values
square = Square(row, player_1, 0)
square_2 = Square(row, player_1, 1)
square_3 = Square(row, player_1, 2)

# player input # of rows
# for i in range(input)
#   row{i} = Row()
# for i in range(input)
#   for loop
#       squares in each row
# 


player_input = input('Which Square do you want?')

for square in row.squares:
    if 0 < int(player_input) <len(row.squares):
        player.enter


        
    


