from collections import deque

def check(arr, sq):
    n = len(arr)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while sq:
        count = 0
        x, y = sq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == '.':
                    count += 1
        if count >= 3:
            return True
    
    return False


T = int(input())
for test_case in range(1, T + 1):
    cnt = 0
    graph, loc = [], deque()
    for i in range(int(input())):
        row = list(input())
        for j in range(len(row)):
            if row[j] == '#':
                loc.append([i, j])
        cnt += row.count('#')
        graph.append(row)
    
    # print(cnt, cnt ** 0.5, int(cnt ** 0.5))
    if cnt == 1:
        print('#{} yes'.format(test_case))
    elif cnt ** 0.5 != int(cnt ** 0.5):
        print('#{} no'.format(test_case))
    
    else:
        if check(graph, loc):
            print('#{} no'.format(test_case))
        else:
            print('#{} yes'.format(test_case))


