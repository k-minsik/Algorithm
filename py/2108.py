import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
# temp = []
# cnt = 0

# for i in set(arr):
#     if arr.count(i) > cnt:
#         temp = []
#         temp.append(i)
#         cnt = arr.count(i)
#     elif arr.count(i) == cnt:
#         temp.append(i)

cnt = Counter(arr).most_common(2)
if len(cnt) > 1:
    if cnt[0][1] == cnt[1][1]:
        temp = cnt[1][0]
    else:
        temp = cnt[0][0]
else:
    temp = cnt[0][0]


print(round(sum(arr) / n))
print(arr[n//2])
# print(temp[1] if len(temp) > 1 else temp[0])
print(temp)
print(arr[-1] - arr[0])
