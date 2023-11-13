# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = []
# for _ in range(n):
#     s, e = map(int, input().split())
#     arr.append([e, s])

# arr.sort()
# answer = 1
# start, end = arr[0][1], arr[0][0]

# for i in range(1, len(arr)):
#     if arr[i][1] >= end:
#         start, end = arr[i][1], arr[i][0]
#         answer += 1

# print(answer)


import sys
input = sys.stdin.readline

n = int(input())
scadule = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x : (x[1], x[0]))

e = scadule[0][1]
count = 1
for ns, ne in scadule[1:]:
    if e <= ns:
        count += 1
        e = ne

print(count)