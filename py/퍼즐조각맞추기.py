from collections import deque
from copy import deepcopy
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x, n, arr, visited):
    dq = deque()
    dq.append([y, x])
    block = [[0, 0]]
    
    while dq:
        cy, cx = dq.popleft()
        
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                if arr[ny][nx] == 1:
                    visited[ny][nx] = 1
                    dq.append([ny, nx])
                    block.append([ny - y, nx - x])
    return block

def bfs2(y, x, n, arr):
    dq = deque()
    dq.append([y, x])
    empty = [[0, 0]]
    
    while dq:
        cy, cx = dq.popleft()
        
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                if arr[ny][nx] == 0:
                    arr[ny][nx] = 2
                    dq.append([ny, nx])
                    empty.append([ny - y, nx - x])
    return empty
    
def bfs3(y, x, n, arr):
    dq = deque()
    dq.append([y, x])
    
    while dq:
        cy, cx = dq.popleft()
        
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                if arr[ny][nx] == 2:
                    arr[ny][nx] = 0
                    dq.append([ny, nx])
    return arr

def rotate(n, arr):
    temp = deepcopy(arr)
    
    for i in range(n):
        for j in range(n):
            temp[j][i] = arr[n - i -1][j]
    
    
    return temp
    
def solution(game_board, table):
    answer = 0
    n = len(game_board)
    
    block = []
    visited_table = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and not visited_table[i][j]:
                visited_table[i][j] = 1
                block.append(bfs(i, j, n, table, visited_table))
                
    temp = deepcopy(game_board)         
    for _ in range(4):
        temp = rotate(n, temp)

        for i in range(n):
            for j in range(n):
                if temp[i][j] == 0:
                    temp[i][j] = 2
                    empty = bfs2(i, j, n, temp)
                    if empty in block:
                        block.remove(empty)
                        answer += len(empty)
                    else:
                        temp = bfs3(i, j, n, temp)
    
    return answer
    
game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]

print(solution(game_board, table))