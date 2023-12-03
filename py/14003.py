import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
visited = {nums[0] : 1}
dq = deque([[nums[0], 0]])

answer = []
while dq:
    print(dq)
    now, idx = dq.popleft()
    tempAnswer = [now]

    for i in range(idx + 1, n):
        if tempAnswer[-1] < nums[i]:
            tempAnswer.append(nums[i])
        
        elif nums[i] < now:
            if nums[i] not in visited:
                dq.append([nums[i], i])
                visited[nums[i]] = 1
    if now == -100:
        print(tempAnswer)

    if len(answer) < len(tempAnswer):
        answer = tempAnswer

print(len(answer))
print(*answer)