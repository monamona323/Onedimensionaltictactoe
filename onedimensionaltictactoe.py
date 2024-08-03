import random

def evaluate(board):
    if 'XXX' in board:
        print ('Computer wins.')
        return 'X'
    elif 'OOO' in board:
        print ('You win.')
        return 'O'
    elif '-' not in board:
        print ('Tie.')
        return '!'
    else:
        return '-'

def move(board, mark, position):
    board_list = list(board)
    board_list[position] = mark
    return ''.join(board_list) 

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
                  print ('You play with O. Your position is: ', position_str)
                  board = move (board, 'O', position_int)
                  return board
        except ValueError:
            print('That is not an integer position.')
            continue

def pc_move (board):
    while True:
        computer_move = random.randrange(20)
        if board[computer_move] == '-':
            board = move(board, 'X', computer_move)
            print ('The computer play with X. Computer position:', computer_move)           
            return board
        else:
            print('This position is already taken.')

def tictactoe_1d(board): 
    while True:
        board = player_move(board)
        print(board)
        result = evaluate(board)
        if result != '-':
            print(f'Result: {result}')
            break

        board = pc_move(board)
        print(board)
        result = evaluate(board)
        if result != '-':
            print(f'Result: {result}')
            break
        
board = '--------------------'
tictactoe_1d(board)
