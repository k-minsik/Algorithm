from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x, n, m, no, graph, visited):
    count = 1
    dq = deque([[y, x]])
    graph[y][x] = no
    visited[y][x] = True
    
    while dq:
        y, x = dq.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    count += 1
                    graph[ny][nx] = no
                    visited[ny][nx] = True
                    dq.append([ny, nx])
    
    return count

def solution(graph):
    answer = 0
    n, m = len(graph), len(graph[0])
    visited = [[False] * m for _ in range(n)]
    oil = [0]
    
    no = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] and not visited[y][x]:
                no += 1
                oil.append(bfs(y, x, n, m, no, graph, visited))
            
    for x in range(m):
        get = set()
        tempAnswer = 0
        for y in range(n):
            get.add(graph[y][x])
        
        for g in get:
            tempAnswer += oil[g]
        
        answer = max(answer, tempAnswer)
            
    for i in graph:
        print(i)

    for i in visited:
        print(i)

    return answer

print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))