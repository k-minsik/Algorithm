def go(n):
    if n == 3:
        return ['***', '* *', '***']
    
    temp = go(n//3)
    ret = []

    for i in temp:
        ret.append(i * 3)
    for i in temp:
        ret.append(i + ' ' * (n//3) + i)
    for i in temp:
        ret.append(i * 3)

    return ret


N = int(input())
answer = go(N)
for i in answer:
    print(i)