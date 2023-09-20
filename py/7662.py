import sys
import heapq
input = sys.stdin.readline

tk = int(input())
for _ in range(tk):
    n = int(input())
    dic = {}
    min_q, max_q = [], []

    for _ in range(n):
        s, num = input().split()
        if s == "I":
            dic[num] = 1
            heapq.heappush(min_q, int(num))
            heapq.heappush(max_q, -int(num))
        else:
            if num in dic:
                del dic[num]
            if int(num) == -1:
                heapq.heappop(min_q)
            else:
                heapq.heappop(max_q)
        
        if not dic:
            min_q, max_q = [], []

    if not dic:
        print("EMPTY")
    else:
        print(-heapq.heappop(max_q), end = " ")
        print(heapq.heappop(min_q))
