gs = 'Start'
board = [[" ", " ", " "],
         [" ", " ", " "],
        [" ", " ", " "]]
X = "X"
O = "O"
turn = 1
def main():
    global board
    print(board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print(9 * "-")
    print(board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print(9 * "-")
    print(board[2][0] + " | " + board[2][1] + " | " + board[2][2])
def win_combo(marker):
    global board
    global gs  
    for c in range (3):
        if board[0][c] == marker and board[1][c] == marker and board[2][c] == marker:
            gs = 'Finale'
            return 
    for a in range(3):
        if board[a][0] == marker and board[a][1] == marker and board[a][2] == marker:
            gs = 'Finale'
            return
    if board[0][0] == marker and board[1][1] == marker and board[2][2] == marker:
        gs = 'Finale'
        return
    if board[a][0] == marker and board[a][1] == marker and board[a][2] == marker:
        gs = 'Finale'
        return

def chooseTurn():
    global turn
    if turn == 1:
        print("Player 1 it's your turn!")
        turn = 2
        # in_1 = input("Player 1 choose the place for your marker:\n")
    elif turn == 2:
        print("Player 2 it is your turn!")
        turn = 1
        # in_2 = input("Player 2 choose the place for your marker:\n")

def marker():
    print("Player 1, please choose marker X or O:")
    choose_m = input()
    if choose_m == "x" or choose_m == "X":
        print("x")
def store_info():
    info = input("Player {} choose the place for your marker:\n".format(str(turn)))
    if info == '7' or info == '8' or info == '9':
        row = 0
        if info == '7':
            col = 0
        if info == '8':
            col = 1
        if info == '9':
            col = 2
    elif info == '4' or info == '5' or info == '6':
        row = 1
        if info == '4':
            col = 0
        if info == '5':
            col = 1
        if info == '6':
            col = 2
    elif info == '1' or info == '2' or info == '3':
        row = 0
        if info == '1':
            col = 0
        if info == '2':
            col = 1
        if info == '3':
            col = 2
        
    # while 
    #     if info == '7' an:
    #         board[0][0]    
    #     elif info == '':
    #         board = 

main()          

# board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# player1 = 'Player 1'
# player2 = 'Player 2'
# turn = player1
# gs = 'Level'
# turn_num = 0
# def check_board(mark):
#    global gs
#    for k in range(3):
#        if board[0][k] ==  mark and board[1][k] == mark  and board[2][k] == mark :
#            gs = 'End'
#            return 'End'
#        for b in range(3):
#            if board[b][0] ==  mark and board[b][1] ==  mark and board[b][2] == mark :
#                gs = 'End'
#                return 'End'
#        if board[0][0] ==  mark and board[1][1] ==  mark and board[2][2] == mark :
#            gs = 'End'
#            return 'End'
#        if board[0][0] ==  mark and board[1][1] ==  mark and board[2][2] == mark :
#            gs = 'End'
#            return 'End'
#        if board[0][2] ==  mark and board[1][1] ==  mark and board[2][0] == mark :
#            gs = 'End' 
#            return 'End'  
#        if board[0][2] ==  mark and board[1][1] ==  mark and board[2][0] == mark :
#            gs = 'End'
#            return 'End' 

# def run_turn():
#    global turn
#    global board
#    global player1
#    global player2
#    global gs
#    global turn_num


#    user_input = input('Enter a number ')
  
#    if user_input == '7' or user_input == '8' or user_input == '9':
#        row_num = 0
#        if user_input == '7':
#            col_num = 0
#        if user_input == '8':
#            col_num = 1
#        if user_input == '9':
#            col_num = 2
#    elif user_input == '4' or user_input == '5' or user_input == '6':
#        row_num = 1
#        if user_input == '4':
#            col_num = 0
#        if user_input == '5':
#            col_num = 1
#        if user_input == '6':
#            col_num = 2
#    elif user_input == "1" or user_input == "2" or user_input == '3':
#        row_num = 2
#        if user_input == '1':
#            col_num = 0
#        if user_input == '2':
#            col_num = 1
#        if user_input == '3':
#            col_num = 2
#    else:
#        print('Thats an invalid numpad key...Try again')
#        return

#    if board[row_num][col_num] == ' ':
#        if turn == player1:
#            board[row_num][col_num] = 'X'
#            if check_board('X') != 'End':
#                turn = player2
#                turn_num += 1
          
#        else:
#           board[row_num][col_num] = 'O'
#           if check_board('O') != 'End':
#               turn = player1
#               turn_num += 1

      
#    else:
#        print('Space is already occupied')
#        return
# def display_board():
#    global board
#    for c in range(3):
#        print('      |      |     ')
#        print('  ' + board[c][0] + '   |   ' +  board[c][1] + '  |  ' + board[c][2] + '  ')
#        print('      |      |     ')
#        if c != 2:
#            print('____________________')

# if gs == 'Main':
#    pass

# elif gs == 'Level':
#    display_board()
#    while gs == 'Level':
#        if input:
#            run_turn()
#            display_board()
#            if turn_num == 9:
#                gs = 'Game_Over'

           
# if gs == 'End':
#    print(turn + ' wins!!!')
# if gs == 'Game_Over':
#    print('TIE')

