# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# arr = set(map(int, input().split()))
# arr2 = set(map(int, input().split()))
# temp = len(arr & arr2)

# print(arr & arr2)
# print(len(arr) + len(arr2) - temp * 2)


import sys
input = sys.stdin.readline

a, b = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

d = {}
for i in A:
    d[i] = 1

answer = a + b
for i in B:
    if i in d:
        answer -= 2

print(answer)