import sys, heapq
input = sys.stdin.readline

arr = []
for _ in range(int(input())):
    heapq.heappush(arr, float(input()))

for _ in range(7):
    print(f'{heapq.heappop(arr):.3f}')
