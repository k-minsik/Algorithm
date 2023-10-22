# answer = 0

# n = int(input())
# m = int(input())
# arr = list(map(int, input().split()))

# if m > 200000:
#     print(0)
# else:
#     s = 0
#     e = n-1
#     arr.sort()
#     while s < e:
#         if arr[s] + arr[e] == m:
#             answer += 1
#             s += 1
#             e -= 1
#         elif arr[s] + arr[e] < m:
#             s += 1
#         else:
#             e -= 1

#     print(answer)


import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
material = sorted(list(map(int, input().split())))
l, r = 0, n - 1

answer = 0
while True:
    if l >= r:
        break

    materialSum = material[l] + material[r]
    if materialSum > m:
        r -= 1
    elif materialSum == m:
        answer += 1
        l += 1
        r -= 1
    elif materialSum < m:
        l += 1

print(answer)