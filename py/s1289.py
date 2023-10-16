for tk in range(1, int(input()) + 1):
    answer = 0
    mem = input()

    if mem[0] == '1':
        change = 1
    else:
        change = 0
    change += mem.count('01')
    change += mem.count('10')


    print('#{} {}'.format(tk, change))