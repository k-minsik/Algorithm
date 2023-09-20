for tk in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    if m % (2 ** n) == 2 ** n - 1:
        print('#{} {}'.format(tk,'ON'))
    else:
        print('#{} {}'.format(tk, 'OFF'))

