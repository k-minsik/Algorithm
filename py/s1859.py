import sys
input = sys.stdin.readline

for tk in range(int(input())):
    days = int(input())
    price = list(map(int, input().split()))
    m = price[-1]
    answer = 0

    for i in price[::-1]:
        if m > i:
            answer += m - i
        else:
            m = i
    
    print('#{} {}'.format(tk+1, answer))




