from collections import deque
def solution(maps):
    answer = []
    row = len(maps)
    col = len(maps[0])
    visited = [[False] * col for _ in range(row)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    q = deque()
    q.append([0, 0, 1])
    visited[0][0] = True
    while q:
        x, y, mv = q.popleft()
        
        if x == row-1 and y == col-1:
            answer.append(mv)
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny < col:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny, mv + 1])

    return min(answer) if answer else -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))