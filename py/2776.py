import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    a = int(input())
    A = list(map(int, input().split()))

    d = {}
    for i in A:
        d[i] = 1
    
    b = int(input())
    B = list(map(int, input().split()))

    for i in B:
        if i in d:
            print(1)
        else:
            print(0)