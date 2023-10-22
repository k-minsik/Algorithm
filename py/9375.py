# tc = int(input())

# for _ in range(tc):
#     bag = {}
#     res = 1
#     for _ in range(int(input())):
#         _, what = map(str, input().split())
#         if what in bag:
#             bag[what] += 1
#         else:
#             bag[what] = 1

#     for _, v in bag.items():
#         res *= (v+1)

#     print(res - 1)

import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())

    item = {}
    for _ in range(n):
        name, type = input().split()
        if type in item:
            item[type] += 1
        else:
            item[type] = 2 # 안입는 거까지 생각

    ret = 1
    for k, v in item.items():
        print(k, v)
        ret *= v
    
    print(ret - 1) # 다안입는거 1 빼기

