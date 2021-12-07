import random
board=[" "]*9
already_placed=[]

def draw_board3():
    print("|----|----|----|")
    print("|    |    |    |")
    print("|   "+board[0]+"| "+board[1]+"  | "+board[2]+"  |")
    print("|    |    |    |")
    print("|----|----|----|")
    print("|    |    |    |")
    print("|   "+board[3]+"| "+board[4]+"  | "+board[5]+"  |")
    print("|    |    |    |")
    print("|----|----|----|")
    print("|    |    |    |")
    print("|   "+board[6]+"| "+board[7]+"  | "+board[8]+"  |")
    print("|    |    |    |")
    print("|----|----|----|")

draw_board3()

def board_copy(board):
     boardcopy = []
     for j in board:
         boardcopy.append(j)
     return boardcopy

def check_win(board,playermark):
    return ((board[0] and board[1] and board[2] == playermark)or
            (board[3] and board[4] and board[5] == playermark)or
            (board[6] and board[7] and board[8] == playermark)or
            (board[0] and board[3] and board[6] == playermark)or
            (board[1] and board[4] and board[7] == playermark)or
            (board[2] and board[5] and board[8] == playermark)or
            (board[0] and board[4] and board[8] == playermark)or
            (board[2] and board[4] and board[6] == playermark)or
            )
def check_draw (board):
    return " "  not in board

def test_win(board,playermark,move):
    bcopy=copyboard(board)
    bcopy[move]=playermark
    return check_win(bcopy,playermark)

def winning(board):
    for i in [0,2,6,8]:
        if board[i]== " ":
            return i
    if board[4] == " ":
        return 4
    for i in [1,3,5,7]:
        if board[i]== " "
        return i

def get_agent_move(board):
        
