import sys
input = sys.stdin.readline

fee = 0
arr = [0 for _ in range(101)]
a, b, c = map(int, input().split())

for _ in range(3):
    t1, t2 = map(int, input().split())
    
    for i in range(t1, t2):
        arr[i] += 1

for i in arr:
    if i == 1:
        fee += a
    elif i == 2:
        fee += b*2
    elif i == 3:
        fee += c*3

print(fee)