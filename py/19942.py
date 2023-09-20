# import sys
# from itertools import combinations
# input = sys.stdin.readline

# n = int(input())
# p, f, c, v = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# ret = 1e9

# for i in range(1, n+1):
#     for temp in combinations(arr, i):
#         tp = 0
#         tf = 0
#         tc = 0
#         tv = 0
#         tm = 0
#         for what in temp:
#             tp += what[0]
#             tf += what[1]
#             tc += what[2]
#             tv += what[3]
#             tm += what[4]

#             if tp >= p and tf >= f and tc >= c and tv >= v:
#                 if ret > tm:
#                     ret = tm
#                     answer = []
#                     for j in temp:
#                         answer.append(arr.index(j) + 1)

# if ret == 1e9:
#     print(-1)
# else:
#     print(ret)
#     print(answer)


import sys
input = sys.stdin.readline

n = int(input())
mp, mf, ms, mv = map(int, input().split())

food = []
for _ in range(n):
    food.append(list(map(int, input().split())))

answer = {}
cost = 1e9
for i in range(1, 1 << n):
    a, b, c, d, cur = 0, 0, 0, 0, 0
    temp = []

    for j in range(n):
        if i & (1 << j):
            temp.append(j+1)
            a += food[j][0]
            b += food[j][1]
            c += food[j][2]
            d += food[j][3]
            cur += food[j][4]

    if a >= mp and b >= mf and c >= ms and d >= mv and cur <= cost:
        cost = cur
        if cost in answer:
            answer[cost].append([sorted(temp)])
        else:
            answer[cost] = sorted([temp])

if cost == 1e9:
    print(-1)
else:
    print(cost)
    answer[cost].sort()
    for q in answer[cost][0]:
        print(q, end = " ")



