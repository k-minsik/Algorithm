# import sys
# input = sys.stdin.readline
# n = int(input());

# for _ in range(n):
#     num = int(input())

#     cnt = 0
#     i = 5
    
#     while i <= num:
#         cnt += num // i
#         i *= 5

#     print(cnt)



import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())

    answer = 0
    five = 5
    while True:
        if five > n:
            break
        
        answer += n // five
        five *= 5

    print(answer)