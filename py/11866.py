from collections import deque

n, k = map(int, input().split())
dq = deque([i for i in range(1, n+1)])
answer = []

while dq:
    for _ in range(k-1):
        dq.append(dq.popleft())
    answer.append(dq.popleft())    

print("<", end = "")
for i in answer[:-1]:
    print(i, end = ", ")
print(answer[-1], end = "")
print(">")
