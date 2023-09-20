import sys
from collections import deque
input = sys.stdin.readline

arr = [deque(input().rstrip()) for _ in range(4)]

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    a -= 1
    temp = [[arr[i][6], arr[i][2]] for i in range(4)]

    if a != 0:
        r = b
        for i in range(a, 0, -1):
            if temp[i - 1][1] != temp[i][0]:
                r *= -1
                arr[i - 1].rotate(r)
            else:
                break

    if a != 3:
        r = b
        for i in range(a, 3):
            if temp[i][1] != temp[i + 1][0]:
                r *= -1
                arr[i + 1].rotate(r)
            else:
                break
    
    arr[a].rotate(b)
    
answer = 0
for i in range(4):
    if arr[i][0] == '1':
        answer += (2 ** i)

print(answer)
