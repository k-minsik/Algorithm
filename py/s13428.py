for tk in range(1, int(input()) + 1):
    n = list(input())
    m, Ma = int(''.join(n)), int(''.join(n))
    
    for i in range(len(n)):
        for j in range(i, len(n)):
            n[i], n[j] = n[j], n[i]
            if n[0] != '0':
                tmp = int(''.join(n))
                if tmp < m:
                    m = tmp
                if tmp > Ma:
                    Ma = tmp
            n[i], n[j] = n[j], n[i]

    print('#{} {} {}'.format(tk, m, Ma))