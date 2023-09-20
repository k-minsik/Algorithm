for tk in range(1, 11):
    answer = 0
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        temp = 0
        for j in range(n):
            if arr[j][i] == 1 and temp == 0:
                temp = 1
            elif arr[j][i] == 2 and temp == 1:
                temp = 0
                answer += 1

    
    print('#{} {}'.format(tk, answer))

