# while True:
#     try:
#         n = int(input())
#     except:
#         break

#     temp = 1
#     cnt = 1
#     while True:
#         if temp % n == 0:
#             print(cnt)
#             break
#         else:
#             temp = (temp * 10 + 1) % n
#             cnt += 1

import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input())
    except:
        break

    compare = 1
    count = 1
    while True:
        if compare % n == 0:
            break

        compare = (compare * 10 + 1) % n
        count += 1
    
    print(count)