from collections import deque

def solution(graph):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    
    n, m = len(graph), len(graph[0])
    visited = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    
    yRed, xRed, yBlue, xBlue = 0, 0, 0, 0
    yRedGoal, xRedGoal, yBlueGoal, xBlueGoal = 0, 0, 0, 0
    
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1:
                yRed, xRed = y, x
            elif graph[y][x] == 2:
                yBlue, xBlue = y, x
            elif graph[y][x] == 3:
                yRedGoal, xRedGoal = y, x
            elif graph[y][x] == 4:
                yBlueGoal, xBlueGoal = y, x
            
    visited[yRed][xRed][yBlue][xBlue] = 1

    dq = deque()
    dq.append([yRed, xRed, yBlue, xBlue])
    
    def both(yRed, xRed, yBlue, xBlue):
        for i in range(4):
            nyRed = yRed + dy[i]
            nxRed = xRed + dx[i]
            
            if (0 <= nyRed < n and 0 <= nxRed < m):
                for j in range(4):
                    nyBlue = yBlue + dy[j]
                    nxBlue = xBlue + dx[j]
                    
                    if (0 <= nyBlue < n and 0 <= nxBlue < m):
                        if visited[nyRed][nxRed][nyBlue][nxBlue]:
                            continue
                        if nyRed == nyBlue and nxRed == nxBlue:
                            # 같은 곳으로
                            continue
                        if nyRed == yBlue and nxRed == xBlue and nyBlue == yRed and nxBlue == xRed:
                            # 자리 체인지
                            continue
                        if graph[nyRed][nxRed] == 5 or graph[nyBlue][nxBlue] == 5:
                            # 벽
                            continue
                        
                        visited[nyRed][nxRed][nyBlue][nxBlue] = visited[yRed][xRed][yBlue][xBlue] + 1
                        dq.append([nyRed, nxRed, nyBlue, nxBlue])
                        
    
    def onlyRed(yRed, xRed, yBlue, xBlue):
        for i in range(4):
            nyRed = yRed + dy[i]
            nxRed = xRed + dx[i]
            
            if (0 <= nyRed < n and 0 <= nxRed < m) and not(visited[nyRed][nxRed][yBlue][xBlue]):
                if graph[nyRed][nxRed] == 5:
                    # 벽
                    continue
                if nyRed == yBlue and nxRed == xBlue:
                    # 같은 자리로
                    continue
                
                visited[nyRed][nxRed][yBlue][xBlue] = visited[yRed][xRed][yBlue][xBlue] + 1
                dq.append([nyRed, nxRed, yBlue, xBlue])
    

    def onlyBlue(yRed, xRed, yBlue, xBlue):
        for i in range(4):
            nyBlue = yBlue + dy[i]
            nxBlue = xBlue + dx[i]
            
            if (0 <= nyBlue < n and 0 <= nxBlue < m) and not(visited[yRed][xRed][nyBlue][nxBlue]):
                if graph[nyBlue][nxBlue] == 5:
                    # 벽
                    continue
                if nyBlue == yRed and nxBlue == xRed:
                    # 같은 자리로
                    continue
                
                visited[yRed][xRed][nyBlue][nxBlue] = visited[yRed][xRed][yBlue][xBlue] + 1
                dq.append([yRed, xRed, nyBlue, nxBlue])
    
    
    red, blue = False, False
    while dq:
        yRed, xRed, yBlue, xBlue = dq.popleft()
        
        if yRed == yRedGoal and xRed == xRedGoal:
            red = True
        if yBlue == yBlueGoal and xBlue == xBlueGoal:
            blue = True
    
        if red and blue:
            break
        elif red and not blue:
            onlyBlue(yRed, xRed, yBlue, xBlue)
        elif blue and not red:
            onlyRed(yRed, xRed, yBlue, xBlue)
        else:
            both(yRed, xRed, yBlue, xBlue)
        
        if red and blue:
            break
        red, blue = False, False
    
    if red and blue:
        return visited[yRedGoal][xRedGoal][yBlueGoal][xBlueGoal] - 1
    else:
        return 0
    
print(solution([[1, 0, 2], [0, 0, 0], [5, 0 ,5], [4, 0, 3]]))