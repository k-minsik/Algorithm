for tk in range(1, int(input())+1):
    s1, s2 = list(input().split())
    s1, s2 = s1*len(s2), s2*len(s1)
    if s1 == s2:
        print('#{} {}'.format(tk, 'yes'))
    else:
        print('#{} {}'.format(tk, 'no'))
