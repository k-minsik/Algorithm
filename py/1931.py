import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    s, e = map(int, input().split())
    arr.append([e, s])

arr.sort()
answer = 1
start, end = arr[0][1], arr[0][0]

for i in range(1, len(arr)):
    if arr[i][1] >= end:
        start, end = arr[i][1], arr[i][0]
        answer += 1

print(answer)

























