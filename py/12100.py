import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def rotate(arr):   # 시계 방향
    temp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j] = arr[n - j - 1][i]

    return temp

def move(arr, d):  # 왼쪽으로 밀기
    temp = deepcopy(arr)
    for _ in range(d):
        temp = rotate(temp)

    for i in range(n):
        here = 0
        for j in range(1, n):
            if temp[i][j]:
                tmp = temp[i][j]
                temp[i][j] = 0
                if temp[i][here] == 0:
                    temp[i][here] = tmp
                elif temp[i][here] == tmp:
                    temp[i][here] = tmp * 2
                    here += 1
                else:
                    here += 1
                    temp[i][here] = tmp

    return temp


def dfs(arr, cnt):
    global answer
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                answer = max(answer, arr[i][j])
        return
    
    for i in range(4): # 왼 아 오 위
        temp = move(arr, i)
        dfs(temp, cnt + 1)

dfs(arr, 0)
print(answer)