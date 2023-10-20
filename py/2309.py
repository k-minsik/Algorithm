# from itertools import combinations
# arr = []
# res = 0

# for i in range(9):
#     temp = int(input())
#     res += temp
#     arr.append(temp)

# for i in list(combinations(arr, 2)):
#     if res - i[0] - i[1] == 100:
#         arr.remove(i[0])
#         arr.remove(i[1])
#         break
    
# arr = sorted(arr, reverse=False)
# for i in arr:
#     print(i)

import sys
input = sys.stdin.readline

graph = [int(input()) for _ in range(9)]
ret = sum(graph)

for i in range(8):
    for j in range(i+1, 9):
        if ret - graph[i] - graph[j] == 100:
            del graph[j]
            del graph[i]
            
            for i in sorted(graph):
                print(i)
            exit()