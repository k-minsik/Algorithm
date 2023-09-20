for tk in range(1, 11):
    n = int(input())
    arr = [list(input()) for _ in range(8)]
    arr2 = list(map(list, zip(*arr)))

    answer = 0

    for i in range(8):
        for j in range(9-n):
            tmp = arr[i][j:j+n]
            tmp2 = arr2[i][j:j+n]
            if tmp == tmp[::-1]:
                answer += 1
            if tmp2 == tmp2[::-1]:
                answer += 1
            


    print('#{} {}'.format(tk, answer))