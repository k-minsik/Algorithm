# import sys
# from itertools import permutations
# sys = sys.stdin.readline

# n = int(input())
# nums = list(map(int, input().split()))
# opers = list(map(int, input().split())) # + - * %
# opers = ['+'] * opers[0] + ['-'] * opers[1] + ['*'] * opers[2] + ['//'] * opers[3]

# M, m = -1e10, 1e10
# for oper in permutations(opers, n - 1):
#     num = nums[0]
#     for i in range(n - 1):
#         if oper[i] == '+':
#             num += nums[i + 1]

#         elif oper[i] == '-':
#             num -= nums[i + 1]

#         elif oper[i] == '*':
#             num *= nums[i + 1]

#         elif oper[i] == '//':
#             num = int(num / nums[i + 1])

    
#     M = max(M, num)
#     m = min(m, num)

# print(M)
# print(m)


n = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split()))
M, m = -1e10, 1e10

def dfs(lv, num, add, sub, mul, div):
    global M, m

    if lv == n:
        M = max(M, num)
        m = min(m, num)

    if add:
        dfs(lv + 1, num + nums[lv], add - 1, sub, mul, div)
    if sub:
        dfs(lv + 1, num - nums[lv], add, sub - 1, mul, div)
    if mul:
        dfs(lv + 1, num * nums[lv], add, sub, mul - 1, div)
    if div:
        dfs(lv + 1, int(num / nums[lv]), add, sub, mul, div- 1)


dfs(1, nums[0], opers[0], opers[1], opers[2], opers[3])
print(M)
print(m)