from random import randrange

board = [[1,2,3],[4,5,6],[7,8,9]]
board[1][1] = 'X'

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[1][0],"  |  ",board[1][1],"  |  ",board[1][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[2][0],"  |  ",board[2][1],"  |  ",board[2][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")



def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    userMove = input("Enter your move: ")
    
    if int(userMove) in make_list_of_free_fields(board):
        if userMove == '1':
            board[0][0] = 'O'
        elif userMove == '2':
            board[0][1] = 'O'
        elif userMove == '3':
            board[0][2] = 'O'
        elif userMove == '4':
            board[1][0] = 'O'
        elif userMove == '5':
            board[1][1] = 'O'
        elif userMove == '6':
            board[1][2] = 'O'
        elif userMove == '7':
            board[2][0] = 'O'
        elif userMove == '8':
            board[2][1] = 'O'
        elif userMove == '9':
            board[2][2] = 'O'
    else:
        print("Invalid input, try again!")
        enter_move(board)

    if(victory_for(board, 'O') == False):
        display_board(board)
        draw_move(board)
    else:
        display_board(board)


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

    fields = []

    for row in board:
        for elements in row:
            if elements == 'O' or elements =='X':
                continue
            fields.append(elements)

    if len(fields) > 0:
        #print(fields)
        return fields
    else: 
        print("Tie!")

    


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game

    if board[0][0] == board[0][1] == board[0][2] == sign :
        print("Player", sign, "Wins!")
        return True
    elif board[0][0] == board[1][0] == board[2][0] == sign :
        print("Player", sign, "Wins!")
        return True
    elif board[0][0] == board[1][1] == board[2][2] == sign :
        print("Player", sign, "Wins!")
        return True
    elif board[0][1] == board[1][1] == board[2][1] == sign :
        print("Player", sign, "Wins!")
        return True
    elif board[0][2] == board[1][1] == board[2][0] == sign :
        print("Player", sign, "Wins!")
        return True
    elif board[0][2] == board[1][2] == board[2][2] == sign :
        print("Player", sign, "Wins!")
        return True
    elif board[1][0] == board[1][1] == board[1][2] == sign :
        print("Player", sign, "Wins!")
        return True
    elif board[2][0] == board[2][1] == board[2][2] == sign :
        print("Player", sign, "Wins!")
        return True
    
    return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    
    oponentMove = randrange(10)
    # print("oponentMove", oponentMove)

    if oponentMove in make_list_of_free_fields(board):
        if oponentMove == 1:
            board[0][0] = 'X'
        elif oponentMove == 2:
            board[0][1] = 'X'
        elif oponentMove == 3:
            board[0][2] = 'X'
        elif oponentMove == 4:
            board[1][0] = 'X'
        elif oponentMove == 5:
            board[1][1] = 'X'
        elif oponentMove == 6:
            board[1][2] = 'X'
        elif oponentMove == 7:
            board[2][0] = 'X'
        elif oponentMove == 8:
            board[2][1] = 'X'
        elif oponentMove == 9:
            board[2][2] = 'X'
    else:
        #print("Invalid input, try again!")
        draw_move(board)

    if(victory_for(board, 'X') == False):
        display_board(board)
        enter_move(board)
    else: 
        display_board(board)
        
    
    
# Start Game #  
display_board(board)
enter_move(board)