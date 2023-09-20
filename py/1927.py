import sys
import heapq
input = sys.stdin.readline

hq = []
for i in range(int(input())):
    x = int(input())

    if x:
        heapq.heappush(hq, x)
    else:
        if hq:
            print(heapq.heappop(hq))
        else:
            print(0)
