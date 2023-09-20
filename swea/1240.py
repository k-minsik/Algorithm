code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

for tk in range(1, int(input())+1):
    r, c = map(int, input().split())

    for _ in range(r):
        row = input()
        if int(row) == 0:
            continue
        else:
            pass