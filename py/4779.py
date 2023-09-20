def go(s, num):
    if num == 0:
        return s

    temp = go(s[:3 ** (num -1)], num - 1)
    temp += " " * (3 ** (num - 1))
    temp += go(s[-(3 ** (num -1)):], num - 1)

    return temp

while True:
    try:
        n = input()
        if n == "":
            break
        n = int(n)
        ss = "-" * (3 ** n)
        print(go(ss, n))

    except EOFError:
        break