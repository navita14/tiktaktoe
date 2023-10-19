from classes.Row import Row
from classes.Square import Square
from classes.Player import Player
import random

def main():

    player_name = input("what is your name?")
    board_size = input("how many rows and columns do you want?")

    player = Player(player_name)

    board = board_creator(board_size, player)



    while True:

        print_board(board)

        player_row_input = input('Which row do you want?')

        for row in Row.rows:
            if int(player_row_input) == row.index:
                player_square_input = input('Which square do you want?')
                for square in row.squares:
                    if int(player_square_input) == square.index:
                        square.value = "X"
        
        print("now it is the computers turn")
        
        cpu_row = random.randint(0, int(board_size) - 1)
        cpu_square = random.randint(0, int(board_size) - 1)

        for row in Row.rows:
            if cpu_row == row.index:
                for square in row.squares:
                    if cpu_square == square.index:
                        square.value = "O"

    
        print_board(board)

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
            Square(row, player, x, x)
            x += 1
        i += 1
        board.append(row.squares)
    return board

def print_board(board):
    i = 0
    for row in board:
        print(i, row, i)
        i += 1      

def set_x_or_0():
    pass

if __name__ == '__main__':
    main()
    





        
    


