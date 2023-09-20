for tk in range(1, int(input())+1):
    n, m, k = map(int, input().split())
    guest = list(map(int, input().split()))
    guest.sort()

    for i in range(n):
        item = (guest[i]//m)*k - (i+1)
        if item < 0:
            result = 'Impossible'
            break
        else:
            result = 'Possible'

    print('#{} {}'.format(tk, result))