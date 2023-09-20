import sys
input = sys.stdin.readline

def rowCheck(r, num):
    for i in range(9):
        if board[r][i] == num:
            return False
        
    return True

def colCheck(c, num):
    for i in range(9):
        if board[i][c] == num:
            return False
        
    return True

def boxCheck(r, c, num):
    for i in range(3):
        for j in range(3):
            if board[((r // 3) * 3) + i][((c // 3) * 3) + j] == num:
                return False
        
    return True


def dfs(depth):
    if depth == len(zeros):
        for i in range(9):
            print(''.join(map(str, board[i])))
        exit()

    y, x = zeros[depth]
    for num in range(1, 10):
        if rowCheck(y, num) and colCheck(x, num) and boxCheck(y, x, num):
            board[y][x] = num
            dfs(depth + 1)
            board[y][x] = 0


board, zeros = [], []
for r in range(9):
    board.append(list(map(int, input().rstrip())))
    for c in range(9):
        if board[r][c] == 0:
            zeros.append([r, c])

dfs(0)