import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
visited = [False for _ in range(100001)]

answer = 0
l, r = 0, 0

while r < n:
    if not visited[arr[r]]:
        visited[arr[r]] = True
        r += 1
    else:
        answer += r - l
        visited[arr[l]] = False
        l += 1

answer += (r - l) * (r - l + 1) // 2
print(answer)