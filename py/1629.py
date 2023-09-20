a, b, c = map(int, input().split())

def go(a, b):
    if b == 1:
        return a % c

    res = go(a, b // 2)
    res = (res * res) % c

    if b % 2 == 1:
        res = (res * a) % c

    return res


print(go(a, b))

pow()