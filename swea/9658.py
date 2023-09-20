for tk in range(1, int(input())+1):
    n = input()

    l = len(n) - 1
    num = round(int(n) /10**l, 1)
    if num == 10.0:
        num = 1.0
        l += 1
        
    answer = str(num)+'*10^'+str(l)

    print('#{} {}'.format(tk, answer))


