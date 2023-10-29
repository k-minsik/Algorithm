# n = int(input())

# i = 0
# num = 666
# while True:
#     if str(num).find('666') >= 0: i += 1
#     if i == n:
#         break
#     num += 1

# print(num)

import sys
input = sys.stdin.readline

n = int(input())

i = 0
answer = 666
while i < n:
    if str(answer).find("666") >= 0:
        i += 1

    answer += 1

print(answer - 1)