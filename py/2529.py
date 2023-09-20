import sys
from collections import deque
input = sys.stdin.readline

def check(a, b, op):
    if a > b and op == '>':
        return True
    elif a < b and op == '<':
        return True
    else:
        return False

def do(idx, temp):
    if idx == n + 1:
        answer.append(temp)
    
    else: 
        for i in range(10):
            if visited[i] == False:
                if idx == 0 or check(int(temp[idx-1]), i, arr[idx-1]):
                    visited[i] = True
                    do(idx + 1, temp + str(i))
                    visited[i] = False


n = int(input())
arr = list(input().split())
visited = [False for _ in range(10)]
answer = []

do(0, "")
print(answer[-1])
print(answer[0])


