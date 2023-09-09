# student name:   Sophie Lin
# student number: 70196886

# A command-line Tic-Tac-Toe game 
import random

board = [' '] * 9 # A list of 9 strings, one for each cell, 
                  # will contain ' ' or 'X' or 'O'
played = set()    # A set to keep track of the played cells 

def init() -> None:
    """ prints the banner messages 
        and prints the intial board on the screen
    """
    print("Welcome to Tic-Tac-Toe!")
    print("You play X (first move) and computer plays O.")
    print("Computer plays randomly, not strategically.")
    printBoard()

def printBoard() -> None:
    """ prints the board on the screen based on the values in the board list """
    #print("    ")
    #print("      |   |      x | x | x")
    #print("    --+---+--    --+---+--")
    #print("      |   |      x | x | x")
    #print("    --+---+--    --+---+--")
    #print("      |   |      x | x | x")
    #print("    ")
    #for i in board:
    print(f"    ")
    print(f"    {board[0]} | {board[1]} | {board[2]}    0 | 1 | 2")
    print(f"    --+---+--    --+---+--")
    print(f"    {board[3]} | {board[4]} | {board[5]}    3 | 4 | 5")
    print(f"    --+---+--    --+---+--")
    print(f"    {board[6]} | {board[7]} | {board[8]}    6 | 7 | 8")
    print(f"    ")

def validCellNum(userInput) -> None:
    """ checks if userInput is a valid cellNum
        cellNum must be an integer, between 0 and 8, and not already taken on the board
        returns True if userInput is valid, else False
    """

    # check if userInput is an integer
    try:
        cellNum = int(userInput)  # try to convert userInput from str to int
    except:
        print("Must be an integer")
        return False
        
    # check if cellNum is in range
    if(cellNum < 0 or cellNum > 8):
        print("Must be a valid cell num")
        return False
    # check if cellNum is already taken
    elif(board[cellNum] != ' '):
        print("Must be an empty cell on the board")
        return False
    else:
        # cellNum is valid
        print(f"You chose cell {cellNum}")
        return True

def playerNextMove() -> None:
    """ prompts the player for a valid cell number, 
        and prints the info and the updated board;
        error checks that the input is a valid cell number 
    """
    while(True):
        userInput = input("Next move for X (state a valid cell num):")
        if(validCellNum(userInput)):
            board[int(userInput)] = 'X'
            printBoard()
            break

def computerNextMove() -> None:
    """ Computer randomly chooses a valid cell, 
        and prints the info and the updated board 
    """
    pass #To Implement

def hasWon(who: str) -> bool:
    """ returns True if who (being passed 'X' or 'O') has won, False otherwise """
    pass #To Implement

def terminate(who: str) -> bool:
    """ returns True if who (being passed 'X' or 'O') has won or if it's a draw, False otherwise;
        it also prints the final messages:
                "You won! Thanks for playing." or 
                "You lost! Thanks for playing." or 
                "A draw! Thanks for playing."  
    """
    pass #To Implement

if __name__ == "__main__":
    # Use as is. 
    init()
    while True:
        playerNextMove()            # X starts first
        if(terminate('X')): break   # if X won or a draw, print message and terminate
        computerNextMove()          # computer plays O
        if(terminate('O')): break   # if O won or a draw, print message and terminate
