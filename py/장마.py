import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = list(map(int, input().split()))
rain = [list(map(int, input().split())) for _ in range(m)]


for i in range(m):
	s, e = rain[i]
	s -= 1

	on = [False for _ in range(n)]
	for j in range(s, e):
		graph[j] += 1
	
	if (i + 1) % 3 == 0:
		for j in range(3):
			s, e = rain[i - j]
			for k in range(s-1, e):
				on[k] = True
				
		for j in range(n):
			if on[j]:
				graph[j] -= 1

print(" ".join(map(str, graph)))