import sys
input = sys.stdin.readline
n = int(input());

for _ in range(n):
    num = int(input())

    cnt = 0
    i = 5
    
    while i <= num:
        cnt += num // i
        i *= 5

    print(cnt)
