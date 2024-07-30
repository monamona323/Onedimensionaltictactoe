import random
board = '--------------------'

'''Write a function evaluate that accepts the string with the board of 1D tic-tac-toe as argument and returns one character based on the state of the game:

"x" – The player who uses crosses (Xs) has won (the board contains xxx)
"o" – The player who uses noughts (Os) has won (the board contains ooo)
"!" – Draw (the board is full but nobody has won)
"-" – Rest (i.e. the game is not finished) '''

# mikor all le a jatek ?
def evaluate(board):
    if 'XXX' in board:
        return 'X'
        print ('Computer wins.')
    elif 'OOO' in board:
        return 'O'
        print ('You win.')
    elif '-' not in board:
        return '!'
        print ('Tie.')
    else:
        return '-'

'''Write a move function that accepts the string with the game board,
 a position number (0-19) and a (x or o) mark and returns a game board
(i.e., a string with the given mark placed in the given position). 
The function header could look something like this:'''

def move (board, mark, position):
    # Returns the game board with the given mark in the given position.
    board_list = list(board)
    board_list[position] = mark
    newboard = move (board, mark, position)
    print (newboard)
    return ''.join(board_list) 

''' Write a player_move function that accepts a string with the game board, 
asks the player which position he wants to play and returns the updated game board with the player's move. 
The function should reject negative or too large numbers or moves to an occupied position. 
If the user has entered a wrong argument, the function should ask again (to get correct answer).'''

def player_move (board):
    while True:
        position_str = input('Which position do you want to play?: ')
        try:
          position_int = int(position_str)

          if position_int < 0 or position_int > 19:
              print ('Please enter a correct position (0-19)')
          else:
              if board [position_int] != '-' :
                  print ('This position is already taken.')
              else:
                  print ('You play position: ',position_str)
                  board = move ( board = board, mark = 'O',position = position_int)
                  print(board)
                  return board
        except:
            ValueError('That is not an integer position.')
            pass
#add options for strings not integers

''' Write a pc_move function that accepts the string with the game board. It will select a position to play, and returns the game board with the computer's move.
Use a simple random "strategy":

Select a random number from 0 to 19.
If the position is empty, place the computer's mark there.
If not, repeat from the first step (select another random number). 
The function header should look something like this:'''

def pc_move (board):
    while True:
        computer_move = random.randrange(20)
        if board[computer_move] == '-':
            board = move(board = board, mark = 'X', position = computer_move)
            print ('The computer selects position:', computer_move)
            print (board)            
        else:
            print('This position is already taken.')
        return board

''' Write a tictactoe_1d function that creates a string with a game board 
and alternately calls the player_move and pc_move functions until someone wins or draws. 
Do not forget to check the status of the game after every turn. '''

def tictactoe_1d(board):
    print('The computer plays with X.')    
    print ('You play with O.')
    board = '--------------------' 
    evaluation = '-'  
    while evaluation =='-':
        board = player_move(board)
        board = pc_move(board)
        evaluation = evaluate(board)

tictactoe_1d(board)