def display_board(board):
    print('\n'*100)
    print(board[7]+ '_|_' + board[8] + '_|_' + board[9])
    print(board[4]+ '_|_' + board[5] + '_|_' + board[6])
    print(board[1]+ ' | ' + board[2] + ' | ' + board[3])

 #input
def player_input():
    marker=input('Pehle bande: X bnega yaan O ? ').upper()
    while("X" not in marker and "O" not in marker):
        print("Enter valid Choice!")
        marker=input('Pehle bande: X bnega yaan O ? ').upper()
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')

 #place marker
def place_marker(board, marker, position):
    board[position]=marker

 #jeeta kya?
def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the left side
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal from left to right
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal from right to left

import random

 #pehle kon?
def choose_first():
    if random.randint(0,1)==0:
        return 'dusra banda'
    else:
        return 'pehla banda'

 #empty space?
def space_check(board,position):
    return board[position]==' '
  
  #full space?
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

 #placeholder
def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position=int(input('kidhr lgaun?: (1-9)'))
        while((position < 1) or  (position > 9)):
            print("Enter valid Choice!")
            position=int(input('kidhr lgaun?: (1-9)'))

    return position

 #firse khelna?
def replay():
    return input('Firse Khelega? Enter Haan ya Na: ').lower().startswith('h') 


 ## main execution ##

print('Lets begin the game, master!!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Kya bolte? Khela shuru kren? Haan ya Na: ')
    
    if play_game.lower()[0] == 'h':
        game_on = True
    elif  play_game.lower()[0] != 'h':
        while (play_game.lower()[0] != "n" and play_game.lower()[0] != "h"):
            print("Enter Valid Choice")
            play_game = input('Kya bolte? Khela shuru kren? Haan ya Na: ')
        if play_game[0]=='n':
            game_on=False
        else:
            game_on=True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
             #pehla banda
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Mubarkhen pehle bande! Tussi great ho!!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Tie hogya yaar!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Dusra banda
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Mubarkhen dusre bande! Tussi great ho!!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Tie hogya yaar!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
