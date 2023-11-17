import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split())) + [-1]
visited = [0] * 14

prev = cards[0]
checkSet = set()
answer = 0 

for cur in cards[1:]:
	if abs(cur - prev) == 1:
		checkSet.add(cur)
		checkSet.add(prev)
	
	elif checkSet:
		answer += 1
		for c in checkSet:
			visited[c] += 1
		checkSet = set()
		
	prev = cur
		
print(answer)
print(*visited[1:])