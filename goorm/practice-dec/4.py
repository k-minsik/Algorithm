import sys
input = sys.stdin.readline

n, k = map(int, input().split())
boxes = []

for _ in range(n):
    size, nums = map(int, input().split())
    boxes.append([size, nums])
boxes.sort(reverse=True)

answer = 0
for i in range(n):
    if k > 0:
        count = min(k, boxes[i][1])
        answer += boxes[i][0] * count * 2
        boxes[i][1] -= count
        k -= count

    answer += boxes[i][0] * boxes[i][1]

print(answer)