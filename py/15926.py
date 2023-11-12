# from collections import deque

# n = int(input())
# s = input().rstrip()

# arr = deque()
# answer = [0 for _ in range(n)]
# for i in range(len(s)):
#     if s[i] == "(":
#         arr.append(i)
#     else:
#         if arr:
#             answer[i] = answer[arr.pop()] = 1

# ret, temp = 0, 0
# for i in answer:
#     if i:
#         temp += 1
#     else:
#         ret = max(ret, temp)
#         temp = 0
# ret = max(ret, temp)

# print(ret)


import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()
stack = []
visited = [False] * len(s)

for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    elif stack:
        visited[i] = True
        visited[stack.pop()] = True

answer, cnt = 0, 0
for i in visited:
    if i:
        cnt += 1
    else:
        answer = max(answer, cnt)
        cnt = 0

print(max(answer, cnt))