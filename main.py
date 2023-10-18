from classes.Row import Row
from classes.Square import Square
from classes.Player import Player

def main():

    player_name = input("what is your name?")
    board_size = input("how many rows and columns do you want?")

    player = Player(player_name)

    board = board_creator(board_size, player)


    while True:

        print_board(board)

        player_row_input = input('Which row do you want?')

        for row in Row.rows:
            if row.index == int(player_row_input):
                index_selection = row.squares

        player_square_selection = input("which square do you want")

        for square in index_selection:
            if square.index == int(player_square_selection):
                change_square_value = input("input your choice")
                square.value = change_square_value


        quit_out = input("end")

        if quit_out == "y":
            return False


def board_creator(board_size, player):
    board = []
    i = 0
    while i < int(board_size):
        row = Row(i)
        x = 0
        while x < int(board_size):
            Square(row, player, x, (i, x))
            x += 1
        i += 1
        board.append(row.squares)
    return board

def print_board(board):
    for row in board:
        print(row)      


if __name__ == '__main__':
    main()
    





        
    


