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

        while True:
            player_row_input = input('Which row do you want?')
            player_square_input = input('Which square do you want?')
            valid_move = False

            for row in Row.rows:
                if int(player_row_input) == row.index:
                    for square in row.squares:
                        if int(player_square_input) == square.index and square.value != "\033[1mX\033[0m" and square.value != "\033[1mO\033[0m":
                            set_x_or_o(square, "\033[1mX\033[0m")
                            valid_move = True
                            break
                    if valid_move:
                        break

            if valid_move:
                break
            else:
                print("Invalid move. Try again.")

        if check_win_condition(board, "\033[1mX\033[0m"):
            print("Player has won!")
            print(board)
            break

        print("Now it is the computer's turn")

        while True:
            cpu_row = random.randint(0, int(board_size) - 1)
            cpu_square = random.randint(0, int(board_size) - 1)
            valid_move = False

            for row in Row.rows:
                if cpu_row == row.index:
                    for square in row.squares:
                        if cpu_square == square.index and square.value != "\033[1mX\033[0m" and square.value != "\033[1mO\033[0m":
                            set_x_or_o(square, "\033[1mO\033[0m")
                            valid_move = True
                            break
                    if valid_move:
                        break

            if valid_move:
                break

        print_board(board)

        if check_win_condition(board, "\033[1mO\033[0m"):
            print("Computer has won!")
            break

        print("Next turn")

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

def set_x_or_o(square, value_input):
    square.value = value_input
    return square.value

def check_win_condition(board, marker):
    for row in board:
        if all(square.value == marker for square in row):
            return True

    for col in range(len(board[0])):
        if all(row[col].value == marker for row in board):
            return True

    if all(board[i][i].value == marker for i in range(len(board))):
        return True

    if all(board[i][len(board) - 1 - i].value == marker for i in range(len(board))):
        return True

    return False

if __name__ == '__main__':
    main()
