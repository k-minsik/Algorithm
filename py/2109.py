# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# arr.sort(key = lambda x : (-x[0], -x[1]))
# visited = [0 for _ in range(10001)]
# visited[0] = 1

# answer = 0
# for p, d in arr:
#     while True:
#         if d == 0:
#             break
#         if not visited[d]:
#             visited[d] = 1
#             answer += p
#             break

#         d -= 1

# print(answer)


import sys
input = sys.stdin.readline

n = int(input())
tutor = [list(map(int, input().split())) for _ in range(n)]
tutor.sort(key = lambda x : (-x[0], -x[1]))
visited = [1] + [0 for _ in range(10000)]

answer = 0
for p, d in tutor:
    if not visited[d]:
        visited[d] = 1
        answer += p
        continue

    while d > 1:
        d -= 1

        if not visited[d]:
            visited[d] = 1
            answer += p
            break

print(answer)