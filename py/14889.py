import sys
sys = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 1e9
for i in range(1 << n):
    temp = int(bin(i)[2:])
    if list(str(temp)).count('1') == n // 2:
        s, l = [], []
        for j in range(n):
            if (1 << j) & i:
                s.append(j)
            else:
                l.append(j)

        ss, ls = 0, 0
        for a in range((n // 2) - 1):
            for b in range(a, n // 2):
                ss += arr[s[a]][s[b]] + arr[s[b]][s[a]]
                ls += arr[l[a]][l[b]] + arr[l[b]][l[a]]
        
        answer = min(answer, abs(ss - ls))

print(answer)