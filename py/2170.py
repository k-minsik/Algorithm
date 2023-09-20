import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()

s,e = arr[0]
answer = 0
for i in range(1, n):
    if arr[i][0] > e:
        answer += e - s
        s, e = arr[i]
    elif arr[i][1] > e:
        e = arr[i][1]

print(answer + e - s)