# import sys
# from collections import deque
# input = sys.stdin.readline

# t = int(input())
# gear = [deque(list(input().rstrip())) for _ in range(t)]
# k = int(input())
# rot = [list(map(int, input().split())) for _ in range(k)]

# for n, d in rot:
#     n -= 1
#     temp = [0 for _ in range(t)]

#     temp[n] = d
#     ld, rd = d, d
#     # 왼쪽
#     for i in range(n - 1, -1, -1):
#         if gear[i][2] != gear[i + 1][6]:
#             ld *= -1
#             temp[i] = ld
#         else:
#             break
#     # 오른쪽
#     for i in range(n + 1, t):
#         if gear[i - 1][2] != gear[i][6]:
#             rd *= -1
#             temp[i] = rd
#         else:
#             break

#     for i in range(t):
#         gear[i].rotate(temp[i])

# answer = 0
# for g in gear:
#     if g[0] == '1':
#         answer += 1
# print(answer)


import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
gears = [deque(list(input().strip())) for _ in range(t)]

k = int(input())
info = [list(map(int, input().split())) for _ in range(k)]

for n, d in info:
    n -= 1
    turnGear = [[n, d]]

    # left
    curN, curD = n, d
    while curN > 0:
        if gears[curN][6] == gears[curN - 1][2]:
            break

        turnGear.append([curN - 1, -curD])
        curN -= 1
        curD *= -1

    # right
    curN, curD = n, d
    while curN < t - 1:
        if gears[curN][2] == gears[curN + 1][6]:
            break

        turnGear.append([curN + 1, -curD])
        curN += 1
        curD *= -1

    for thisGear, rot in turnGear:
        gears[thisGear].rotate(rot)

answer = 0
for gear in gears:
    answer += int(gear[0])
print(answer)