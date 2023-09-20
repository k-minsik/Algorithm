for tk in range(1, 11):
    answer = []
    n = int(input())
    arr, sr, sc = [], [], []
    s1, s2 = 0, 0

    for i in range(100):
        row = list(map(int, input().split()))
        sr.append(sum(row))
        arr.append(row)
        # c[i] += row[i]
        s1 += arr[i][i]
        s2 += arr[i][99-i]

    for i in list(map(list, zip(*arr))):
        sc.append(sum(i))

    answer.append(max(sr))
    answer.append(max(s1, s2))
    answer.append(max(sc))

    print('#{} {}'.format(tk, max(answer)))


