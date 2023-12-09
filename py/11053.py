import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
memo = [0]

for i in arr:
    if memo[-1] < i:
        memo.append(i)
    
    else:
        l, r = 0, len(memo)

        while l < r:
            m = (l + r) // 2

            if memo[m] < i:
                l = m + 1
            else:
                r = m
            
        memo[r] = i

print(len(memo) - 1)