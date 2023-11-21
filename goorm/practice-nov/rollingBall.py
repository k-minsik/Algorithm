# import sys
# from collections import deque
# from copy import deepcopy
# input = sys.stdin.readline

# n, s, k = map(int, input().split())
# dq = deque([s - 1])

# def move(x):
# 	initX = x
# 	nx = []
	
# 	while 0 <= x - 1 < n and graph[x-1] <= graph[x]:
# 		x -= 1
# 	nx.append(x)
	
# 	x = initX
# 	while 0 <= x - 1 < n and graph[x+1] <= graph[x]:
# 		x += 1
# 	nx.append(x)
	
# 	return nx
	
# x = [s - 1]

# for _ in range(k):
# 	graph = list(map(int, input().split()))
# 	nx = []
	
# 	for i in x:
# 		nx += move(i)
# 	x = nx
	
# answer = [0] * n
# for x in nx:
# 	answer[x] = 1

# print(*answer)

import sys
input = sys.stdin.readline

n, s, k = map(int, input().split())
positions = {s - 1}  # 초기 구슬 위치

for _ in range(k):
    heights = list(map(int, input().split()))
    next_positions = set()

    for pos in positions:
        # 왼쪽으로 이동
        left = pos
        while left > 0 and heights[left - 1] <= heights[left]:
            left -= 1
        next_positions.add(left)

        # 오른쪽으로 이동
        right = pos
        while right < n - 1 and heights[right + 1] <= heights[right]:
            right += 1
        next_positions.add(right)

    positions = next_positions  # 다음 단계의 위치를 업데이트

# 최종 위치 출력
answer = [0] * n
for pos in positions:
    answer[pos] = 1

print(*answer)