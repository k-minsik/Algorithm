# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]
# dp[0][0][1] = 1 # [방향][y][x]

# for i in range(2, n):
#     if arr[0][i] == 0:
#         dp[0][0][i] = dp[0][0][i - 1]

# for y in range(1, n):
#     for x in range(2, n):
#         if not(arr[y-1][x-1] or arr[y][x-1] or arr[y-1][x] or arr[y][x]):
#             dp[1][y][x] = dp[0][y-1][x-1] + dp[1][y-1][x-1] + dp[2][y-1][x-1]
        
#         if not arr[y][x]:
#             dp[0][y][x] = dp[0][y][x-1] + dp[1][y][x-1]
#             dp[2][y][x] = dp[1][y-1][x] + dp[2][y-1][x]

# answer = 0
# for i in range(3):
#     answer += dp[i][n-1][n-1]
# print(answer)

n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse= True)
answer = 0
for i, j in zip(a, b):
    answer += i * j
print(answer)
