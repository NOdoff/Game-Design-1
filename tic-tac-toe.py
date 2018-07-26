gs = "main"
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
def chooseTurn():
    if turn == 1:
        print("Player 1 it's your turn!")
        # in_1 = input("Player 1 choose the place for your marker:\n")
    elif turn == 2:
        print("Player 2 it is your turn!")
        # in_2 = input("Player 2 choose the place for your marker:\n")

def marker():
    print("Player 1, please choose marker X or O:")
    choose_m = input()
    if choose_m == "x" or choose_m == "X":
        print("x")
def store_info():
    info = input("Player {} choose the place for your marker:\n".format(str(turn)))
    # while 
    #     if info == '7' an:
    #         board[0][0]    
    #     elif info == '':
    #         board = 

main()          