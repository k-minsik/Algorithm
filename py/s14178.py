for tk in range(1, int(input()) + 1):
    n, d = map(int, input().split())
    print('#{} {}'.format(tk, n//(d*2 + 1) + 1 if n %(d*2 + 1) != 0 else n//(d*2 + 1)))