
T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    arr = sorted(arr)

    print('#{} {}'.format(test_case, round(sum(arr[1:-1])/8)))


