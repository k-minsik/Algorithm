for tk in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))
    l, r = 0, 99

    for _ in range(dump):
        arr = sorted(arr)
        arr[0] += 1
        arr[99] -= 1

    print(arr)

    print('#{} {}'.format(tk, max(arr)-min(arr)))