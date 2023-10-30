# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))
# answer = [-1 for _ in range(n)]
# st = []

# for i in range(n):
#     temp = arr[i]

#     while st and arr[st[-1]] < temp:
#         answer[st.pop()] = temp

#     st.append(i)
    
# for i in answer:
#     print(i, end = " ")


import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

answer = [-1 for _ in range(n)]
stack = []
for i in range(n):
    now = nums[i]

    while stack and nums[stack[-1]] < now:
        answer[stack.pop()] = now

    stack.append(i)

print(*answer)