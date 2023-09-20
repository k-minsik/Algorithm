import sys
from heapq import heappop, heappush
sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()

temp = []
for d, c in arr:
    heappush(temp, c)
    if len(temp) > d:
        heappop(temp)

print(sum(temp))