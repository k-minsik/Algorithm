def check(m, n, board):
    temp = []

    for i in range(m - 1):
        for j in range(n - 1):
            if board[i][j] != '0' and board[i][j] == board[i + 1][j] and board[i][j] == board[i][j + 1] and board[i][j] == board[i + 1][j + 1]:
                temp.append([i, j])
                temp.append([i + 1, j])
                temp.append([i, j + 1])
                temp.append([i + 1, j + 1])

    return temp

def do(board, temp):
    ret = 0
    for y, x in temp:
        if board[y][x] != '0':
            ret += 1
        board[y][x] = '0'

    board_temp = []
    for i in zip(*board):
        cnt = i.count('0')
        temp2 = []
        for j in i:
            if j != '0':
                temp2.append(j)
        board_temp.append(['0'] * cnt + temp2)

    ret_board = []
    for i in zip(*board_temp):
        ret_board.append(list(i))

    return ret, ret_board

def solution(m, n, board_temp):
    answer = 0

    board = []
    for i in board_temp:
        board.append(list(i))

    while True:
        temp = check(m, n, board)
        if not temp:
            break

        ret, board = do(board, temp)
        answer += ret

    return answer



print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))