from classes.Row import Row
from classes.Square import Square
from classes.Player import Player

#three rows
row_1 = Row(0)
row_2 = Row(1)

player_1 = Player("Nav")

#row 1 square values
square_1 = Square(row_1, player_1, 0)
square_2 = Square(row_1, player_1, 1)
square_3 = Square(row_1, player_1, 2)

square_4 = Square(row_2, player_1, 0)
square_5 = Square(row_2, player_1, 1)
square_6 = Square(row_2, player_1, 2)


def main():

    while True:
        print(row_1.squares)
        print(row_2.squares)

        player_row_input = input('Which row do you want?')

        for row in Row.rows:
            if row.index == int(player_row_input):
                index_selection = row.squares

        player_square_selection = input("which square do you want")

        for square in index_selection:
            if square.index == int(player_square_selection):
                change_square_value = input("input your choice")
                square.value = change_square_value

        print(row_1.squares)
        print(row_2.squares)

        quit_out = input("end")

        if quit_out == "y":
            return False

if __name__ == '__main__':
    main()
    





        
    


