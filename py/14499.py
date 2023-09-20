import sys
input = sys.stdin.readline

r, c, y, x, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
dice = [0, 0, 0, 0, 0, 0] # dice[1] : 윗 , dice[3] : 아
do = list(map(int, input().split()))
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

def roll(d):
    if d == 2: # North
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]
    
    elif d == 0: # East
        dice[1], dice[3], dice[4], dice[5] = dice[5], dice[4], dice[1], dice[3]

    elif d == 3: # South
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
    
    elif d == 1: # West
        dice[1], dice[3], dice[4], dice[5] = dice[4], dice[5], dice[3], dice[1]


for i in do:
    i -= 1
    ny = y + dy[i]
    nx = x + dx[i]

    if 0 <= ny < r and 0 <= nx < c:
        roll(i)
        print(dice[1])
        y, x = ny, nx

        if arr[y][x]:
            dice[3] = arr[y][x]
            arr[y][x] = 0
        else:
            arr[y][x] = dice[3]
    
    else:
        continue