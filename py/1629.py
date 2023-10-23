# a, b, c = map(int, input().split())

# def go(a, b):
#     if b == 1:
#         return a % c

#     res = go(a, b // 2)
#     res = (res * res) % c

#     if b % 2 == 1:
#         res = (res * a) % c

#     return res


# print(go(a, b))


import sys
input = sys.stdin.readline

def func(a, b, c):
    if b == 1:
        return a % c
    
    next = func(a, b // 2, c)

    if b % 2 == 0:
        return next * next % c
    else:
        return a * next * next % c

a, b, c = map(int, input().split())
print(func(a, b, c))