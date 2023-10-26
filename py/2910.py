# n, c = map(int, input().split())
# arr = list(map(int, input().split()))

# cnt = {}

# for i in range(len(arr)):
#     if arr[i] in cnt:
#         cnt[arr[i]][0] += 1
#     else:
#         cnt[arr[i]] = [1, i]

# cnt = sorted(cnt.items(), key = lambda x: (-x[1][0], x[1][1]))

# for k, v in cnt:
#     for _ in range(v[0]):
#         print(k, end = ' ')


import sys
input = sys.stdin.readline

n, c = map(int, input().split())
array = list(map(int, input().split()))

count = {}
for i in range(n):
    if array[i] in count:
        count[array[i]][1] += 1
    else:
        count[array[i]] = [i, 1]

answer = ""
for k, v in sorted(count.items(), key = lambda x : (-x[1][1], x[1][0])):
    answer += (str(k) + " ") * v[1]

print(answer.rstrip())