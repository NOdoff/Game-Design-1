gs = "main"
board = [["1", " ", " "],
         [" ", " ", " "],
        [" ", " ", " "]]
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
    elif turn == 2:
        print("Player 2 it is your turn!")
def store_int():
    in_1 = input("Player 1 choose the place for your marker:")
main()          