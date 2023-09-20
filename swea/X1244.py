for tk in range(1, int(input()) + 1):
    n, c = map(int, input().split())
    ns = list(str(n))
    print(ns)
    while c != 0:
        for i in range(len(ns)):
            for j in range(i+1, len(ns)):
                ns[i], ns[j] = ns[j], ns[i]
                if int(''.join(ns)) > n:
                    answer = int(''.join(ns))

                ns[i], ns[j] = ns[j], ns[i]
        c -= 1

    print('#{} {}'.format(tk, answer))

