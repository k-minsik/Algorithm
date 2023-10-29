# import sys
# input = sys.stdin.readline

# def dfs(i):
#     cnt = 1
#     visited[i] = 1
#     st = [i]

#     while st:
#         cur = st.pop()
#         for c in arr[cur]:
#             if visited[c] == 0:
#                 cnt += 1
#                 st.append(c)

#     return cnt


# n, m = map(int, input().split())
# arr = [[] for _ in range(n+1)]
# mx = -1

# for _ in range(m):
#     a, b = map(int, input().split())
#     arr[b].append(a)

# answer = []
# for i in range(1, n+1):
#     visited = [0 for _ in range(n+1)]
#     temp = dfs(i)
#     if temp > mx:
#         answer = []
#         answer.append(i)
#         mx = temp
#     elif temp == mx:
#         answer.append(i)
#     else:
#         continue
    
      
# for i in answer:
#     print(i, end = " ")


import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

def bfs(start):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    count = 1

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1

    return count

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

maxHaking = -1
answer = []
for i in range(1, n + 1):
    canHaking = bfs(i)
    if canHaking > maxHaking:
        maxHaking = canHaking
        answer = [i]
    elif canHaking == maxHaking:
        answer.append(i)

print(*answer)