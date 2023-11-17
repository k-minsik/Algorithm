import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

n, s, k = map(int, input().split())
dq = deque([s - 1])

def move(x):
	initX = x
	nx = []
	
	while 0 <= x - 1 < n and graph[x-1] <= graph[x]:
		x -= 1
	nx.append(x)
	
	x = initX
	while 0 <= x - 1 < n and graph[x+1] <= graph[x]:
		x += 1
	nx.append(x)
	
	return nx
	
x = [s - 1]

for _ in range(k):
	graph = list(map(int, input().split()))
	nx = []
	
	for i in x:
		nx += move(i)
	x = nx
	
answer = [0] * n
for x in nx:
	answer[x] = 1

print(*answer)