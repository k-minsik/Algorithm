T = int(input())
for tk in range(1, T+1):
    num = input()
    n = sorted(list(map(int, num)))
    m = max(n)
    for i in range(2, m+2):
        temp = sorted(list(map(int, str(int(num) * i))))
        if i == m+1:
            print('#{} {}'.format(tk, 'impossible'))
        if n == temp:
            print('#{} {}'.format(tk, 'possible'))
            break