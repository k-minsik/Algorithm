import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(1 << n)] for _ in range(n)]

def tsp(here, visited):
    if visited == (1 << n) - 1:
        if arr[here][0]:
            return arr[here][0]
        else:
            return 1e9
        
    if dp[here][visited] != -1:
        return dp[here][visited]
    
    answer = 1e9
    for i in range(n):
        if visited & (1 << i):
            continue
        if arr[here][i] == 0:
            continue
        answer = min(answer, tsp(i, visited | (1 << i)) + arr[here][i])

    return answer
    
print(tsp(0, 1))
