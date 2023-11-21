# import sys
# input = sys.stdin.readline

# n = int(input())
# cards = list(map(int, input().split())) + [-1]
# visited = [0] * 14

# prev = cards[0]
# checkSet = set()
# answer = 0 

# for cur in cards[1:]:
# 	if abs(cur - prev) == 1:
# 		checkSet.add(cur)
# 		checkSet.add(prev)
	
# 	elif checkSet:
# 		answer += 1
# 		for c in checkSet:
# 			visited[c] += 1
# 		checkSet = set()
		
# 	prev = cur
		
# print(answer)
# print(*visited[1:])

import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

# 각 숫자 카드가 몇 번 계단세트에 포함되었는지를 저장할 리스트
visited = [0] * 14

# 계단세트의 개수
answer = 0

# 현재 계단세트에 포함된 카드를 추적하기 위한 임시 리스트
current_set = []

for i in range(n):
    # 현재 카드가 이전 카드와 연속적인지 확인 (계단세트의 시작 또는 계속)
    if i == 0 or abs(cards[i] - cards[i - 1]) == 1:
        current_set.append(cards[i])
    else:
        # 새로운 계단세트가 시작되므로 이전 세트를 처리
        answer += 1
        for card in current_set:
            visited[card] += 1
        current_set = [cards[i]]

# 마지막 계단세트 처리
if current_set:
    answer += 1
    for card in current_set:
        visited[card] += 1

print(answer)
print(*visited[1:])