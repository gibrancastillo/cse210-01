'''
Author: Brother Castillo
File: tictactoe.py
Purpose: Tic-Tac-Toe is a game in which two players seek in alternate turns to complete a row, a column, 
         or a diagonal with either three x's or three o's drawn in the spaces of a grid of nine squares.
'''


def main():
    '''
    Pending
    '''
    player = active_player("")
    board = create_board_grid()
    
    while not (has_winner(board) or is_a_draw(board)):
        display_board_grid(board)
        take_turn(player, board)
        player = active_player(player)
    
    display_board_grid(board)
    print("Good game. Thanks for playing!")


def create_board_grid():
    '''
    Creates the board grid using a list with each location, see interface below.
    The game is played on a grid that is three squares by three squares.
        1|2|3
        -+-+-
        4|5|6
        -+-+-
        7|8|9
    Return: a list
    '''
    board_grid = []
    for location in range(9):
        board_grid.append(location + 1)
    
    return board_grid


def display_board_grid(board_grid):
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
    '''
    print(f"\n{board_grid[0]}|{board_grid[1]}|{board_grid[2]}")
    print("-+-+-")
    print(f"{board_grid[3]}|{board_grid[4]}|{board_grid[5]}")
    print("-+-+-")
    print(f"{board_grid[6]}|{board_grid[7]}|{board_grid[8]}\n")

    print()
    print(board_grid)
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
    location =  int(input(f"{active_player}'s turn to choose a square (1-9): "))
    board_grid[location - 1] = active_player


def is_a_draw(board_grid):
    '''
    Determine if all nine squares are full and neither player has three in a row, the game ends in a draw.
    Parameters:
        board_grid - A reference for a list
    Returns: a boolean
    '''
    for location in range(9):
        if(board_grid[location] != "x" and board_grid[location] != "o"):
            return False
    return True


def has_winner(board_grid):
    '''
    Determine if a player, has three of their marks in a row (vertically, horizontally, or diagonally), is the winner.
    Parameters:
        board_grid - A reference for a list
    Returns: a boolean
    '''
    # board_grid = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # 0|1|2
    # -+-+-
    # 3|4|5
    # -+-+-
    # 6|7|8
    return (board_grid[0] == board_grid[1] == board_grid[2] or
            board_grid[3] == board_grid[4] == board_grid[5] or
            board_grid[6] == board_grid[7] == board_grid[8] or
            board_grid[0] == board_grid[3] == board_grid[6] or
            board_grid[1] == board_grid[4] == board_grid[7] or
            board_grid[2] == board_grid[5] == board_grid[8] or
            board_grid[0] == board_grid[4] == board_grid[8] or
            board_grid[2] == board_grid[4] == board_grid[6])


# If this file was executed like this: % python3 tictactoe.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    # Start this program by calling the main function.
    main()