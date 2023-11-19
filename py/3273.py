# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))
# x = int(input())
# arr.sort()

# answer = 0
# l, r = 0, n-1
# while l < r:
#     if arr[l] + arr[r] == x:
#         answer +=1
#         r -= 1
#     elif arr[l] + arr[r] > x:
#         r -= 1
#     else:
#         l += 1

# print(answer)


import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())

answer = 0
s, e = 0, n - 1
while s < e:
    temp = nums[s] + nums[e]
    if temp == x:
        answer += 1
        s += 1
        e -= 1
        continue

    if temp < x:
        s += 1
    
    elif temp > x:
        e -= 1

print(answer)