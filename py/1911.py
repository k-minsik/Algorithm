# import sys
# input = sys.stdin.readline

# n, l = map(int, input().split())
# arr = sorted([list(map(int, input().split())) for _ in range(n)])

# answer = 0
# idx = 0

# for s, e in arr:
#     if s > idx:
#         idx = s
    
#     dist = e - idx
#     temp = dist // l
#     if dist % l:
#         temp += 1

#     idx += l * temp
#     answer += temp

# print(answer)

import sys, math
input = sys.stdin.readline

n, l = map(int, input().split())
hole = sorted([list(map(int, input().split())) for _ in range(n)])

answer, endPoint = 0, 0
for s, e in hole:
    if s > endPoint:
        endPoint = s

    holeLength = e - endPoint
    need = math.ceil(holeLength / l)

    endPoint += l * need
    answer += need

print(answer)