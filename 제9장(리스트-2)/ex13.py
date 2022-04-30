# ########################################################################

board = []

def initBoard(cnt):
    global board
    for row in range(cnt):
        board += [ ["□"] * cnt]

def printBoard(mylist):
    for row in range(len(mylist)):
        for col in range(len(mylist[row])):
            print(mylist[row][col], end=" ")
        print("")

def checkerBoard(mylist):
    for row in range(len(mylist)):
        for col in range(len(mylist[row])):
            if(row + col) % 2 == 0:
                board[row][col] = "■"

if __name__ == "__main__":
    cnt = 20
    # printList(board)
    initBoard(cnt)
    checkerBoard(board)
    printBoard(board)