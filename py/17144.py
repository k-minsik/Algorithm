import sys
from copy import deepcopy
input = sys.stdin.readline

r, c, t = map(int, input().split())
arr = []
air = []
for i in range(r):
    temp = list(map(int, input().split()))
    if -1 in temp:
        air.append([i, temp.index(-1)])
    arr.append(temp)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def spread(arr):
    temp = [[0 for _ in range(c)] for _ in range(r)]
    for y in range(r):
        for x in range(c):
            cnt = 0
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= ny < r and 0 <= nx < c and arr[ny][nx] != -1:
                    temp[ny][nx] += int(arr[y][x] / 5)
                    cnt += 1
            temp[y][x] += arr[y][x] - int(arr[y][x] / 5) * cnt
    return temp

def rotate(arr):
    temp = deepcopy(arr)

    y, x = air[0]
    temp[y][1] = 0
    for i in range(2, c):
        temp[y][i] = arr[y][i - 1]
    
    for i in range(y-1, -1, -1):
        temp[i][c-1] = arr[i + 1][c-1]
    
    for i in range(c-2, -1, -1):
        temp[0][i] = arr[0][i + 1]

    for i in range(1, y):
        temp[i][0] = arr[i - 1][0]


    y, x = air[1]
    temp[y][1] = 0
    for i in range(2, c):
        temp[y][i] = arr[y][i - 1]

    for i in range(y+1, r):
        temp[i][c-1] = arr[i - 1][c-1]

    for i in range(c-2, -1, -1):
        temp[r-1][i] = arr[r-1][i + 1]

    for i in range(r-2, y, -1):
        temp[i][0] = arr[i + 1][0]

    return temp

answer = 2
for _ in range(t):
    arr = spread(arr)
    arr = rotate(arr)

for i in arr:
    answer += sum(i)
print(answer)
