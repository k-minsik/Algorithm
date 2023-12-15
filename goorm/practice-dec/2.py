import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
stringA = deque(input().strip())
command = list(input().strip())

answer = ""
for c in command:
    if c == "L":
        answer += stringA.popleft()

    elif c == "R":
        answer += stringA.pop()

print(answer)