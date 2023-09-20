for tk in range(1, int(input())+1):
    answer = 0
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]

    mid = int(n / 2)

    for i in range(n):
        rng = int(abs(i - mid))
        answer += sum(farm[i][rng:n-rng])


    print('#{} {}'.format(tk, answer))


