'''
Author: Brother Castillo
File: tictactoe.py
Purpose: Tic-Tac-Toe is a game in which two players seek in alternate turns to complete a row, a column, 
         or a diagonal with either three x's or three o's drawn in the spaces of a grid of nine squares.
'''
# Import the standard plugins or utils obtain OS utils
import os, shutil
import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)


def main():
    '''
    Pending
    '''
    clear_console_display_title()
    board_size = select_board_grid_size()
    player = active_player("")
    board = create_board_grid(board_size)
    
    # Evaluates whether there is a winner or a tie
    while not (has_winner(board_size, board) or is_a_draw(board_size, board)):
        print("++++++++++++++++++++++++++++++++++++")
        display_board_grid(board, board_size)
        take_turn(player, board)
        # swapping the turn or flipping player
        player = active_player(player)
    
    # showing the final view of board
    display_board_grid(board, board_size)

    # checking whether current player is won or not
    if(has_winner(board_size, board)):
        print(f"Player {active_player(player)} wins the game!")
    else:
        print("Match Draw!")

    print("Good game. Thanks for playing!\n")


def clear_console_display_title():
    """
    Clear console or terminal screen according to the OS and
    dispplay title center based on the size of their shell
    """
    # Obtain number of column of the shell
    terminalSize = shutil.get_terminal_size().columns

    if os.name in ('nt', 'dos'):
        os.system('cls')
    else:
        os.system('clear')
    
    # Print title center based on the size of their shell
    tittle = 'W02 Prove Milestone  - \U0001f600  \n'
    print(tittle.center(terminalSize))


def select_board_grid_size():
    '''
    Enhanced board size (4x4, 5x5, 6x6 grid, or user selected!)
    '''
    board_grid_size = int(input("Enter board grid size (3 - 3x3, 4 - 4x4, 5 - 5x5, 6 - 6x6, etc): "))

    while board_grid_size < 3:
        board_grid_size = int(input("Enter board grid size greater than two: "))

    return board_grid_size


def create_board_grid(board_size):
    '''
    Creates the board grid using a list with each location, see interface below.
    The game is played on a grid that is three squares by three squares.
        1|2|3
        -+-+-
        4|5|6
        -+-+-
        7|8|9
    Parameters:
        board_size - An integer
    Return: a list
    '''
    locations = board_size ** 2
    board_grid = []
    for location in range(locations):
        board_grid.append(location + 1)
    
    return board_grid


def display_board_grid(board_grid, board_size):
    '''
    Displays the board grid using a reference for list with each location, see interface below.
    The game is played on a grid that is three squares by three squares.
        1|2|3
        -+-+-
        4|5|6
        -+-+-
        7|8|9
    Parameters:
        board_grid - A list
        board_size - An integer
    '''
    for i in range(0, len(board_grid), board_size):
        if board_size == 3:
            print(f"{board_grid[i]}{Fore.WHITE}|{board_grid[i + 1]}{Fore.WHITE}|{board_grid[i + 2]}")

            if i != 6:
                print("-+-+-")
        elif board_size == 4:
            print(f"{board_grid[i]}{Fore.WHITE}|{board_grid[i + 1]}{Fore.WHITE}|{board_grid[i + 2]}{Fore.WHITE}|{board_grid[i + 3]}")

            if i != 12:
                print("-+-+-+-")
    
    print()


def active_player(current_player):
    '''
    Return active player. Player one uses x's. Player two uses o's.
    Parameter:
        current_player - A string
    Return: A string
    '''
    if current_player == "" or current_player == "o":
        return "x"
    elif current_player == "x":
        return "o"


def take_turn(active_player, board_grid):
    '''
    Allows the active player to take a turn in the tic tack toe board game.
    Parameters:
        active_player - A string value
        board_grid - A reference for a list
    Returns: nothing
    '''
    location =  int(input(f"Player {active_player}'s turn to choose a square (1-9): "))
    
    while(type(board_grid[location - 1]) == str):
        location =  int(input(f"Player {active_player}'s turn to choose a square (1-9) that is not used: "))
    
    board_grid[location - 1] = f"{Fore.RED}{active_player}" if active_player == "x" else f"{Fore.CYAN}{active_player}"


def is_a_draw(board_size, board_grid):
    '''
    Determine if all nine squares are full and neither player has three in a row, the game ends in a draw.
    Parameters:
        board_size - An integer
        board_grid - A reference for a list
    Returns: a boolean
    '''
    locations = board_size ** 2

    for location in range(locations):
        if(board_grid[location] != "x" and board_grid[location] != "o"):
            return False
    
    return True


def has_winner(board_size, board_grid):
    '''
    Determine if a player, has three of their marks in a row (vertically, horizontally, or diagonally), is the winner.
    Parameters:
        board_size - An integer
        board_grid - A reference for a list
    Returns: a boolean
    '''
    # x|x|o
    # -+-+-
    # x|o|o
    # -+-+-
    # 7|x|o
    #
    # ['x', 'x', 'o', 'x', 'o', 'o', 7, 'x', 'o']
    # Tic Tac Toe - Winning Arrangements, checking rows, columns, and diagonals
    has_winner = False

    # horizontal
    for i in range(0, len(board_grid), board_size):
        has_winner = (board_grid[i] == board_grid[i + 1] == board_grid[i + 2])

        if has_winner:
            return has_winner
    
    # vertical
    for i in range(board_size):
        has_winner = (board_grid[i] == board_grid[i + board_size] == board_grid[i + (board_size * 2)])

        if has_winner:
            return has_winner
    
    # diagonal
    for i in range(board_size - 1):
        has_winner = (board_grid[i * 2] == board_grid[i + board_size + 1] == board_grid[i + (board_size * 2)])

        if has_winner:
            return has_winner
    
    return has_winner


# If this file was executed like this: % python3 tictactoe.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    # Start this program by calling the main function.
    main()