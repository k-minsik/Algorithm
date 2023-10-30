# import sys
# input = sys.stdin.readline

# n = int(input())
# t = [[] for _ in range(n)]
# temp = list(map(int, input().split()))
# e = int(input())


# for i in range(n):
#     if temp[i] == -1:
#         root = i
#     else:
#         t[temp[i]].append(i)

# answer = 0 
# st = [root]
# if e == root: print(0)
# else:
#     while st:
#         cur = st.pop()
#         if len(t[cur]) != 0:
#             if len(t[cur]) == 1 and t[cur][0] == e:
#                 print(t[cur])
#                 answer += 1
#             else:
#                 for c in t[cur]:
#                     if c != e:
#                         st.append(c)
#         else:
#             answer += 1

#     print(answer)

# print(t)


import sys
input = sys.stdin.readline

n = int(input())
tree = list(map(int, input().split()))
graph = [[] for _ in range(n)]

for i in range(n):
    if tree[i] == -1:
        root = i
    else:
        graph[tree[i]].append(i)

deleteNode = int(input())
if deleteNode == 0:
    print(0)
    exit()

parentNode = tree[deleteNode]
graph[parentNode].remove(deleteNode)

answer = 0
stack = [root]
while stack:
    now = stack.pop()

    if len(graph[now]) == 0:
        answer += 1
        continue

    for child in graph[now]:
        stack.append(child)

print(answer)