import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
a = input().rstrip()
b = input().rstrip()

if a in b:
    print('secret')
else:
    print('normal')