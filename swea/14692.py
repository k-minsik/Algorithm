T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    print('#{} {}'.format(test_case, 'Alice' if n%2 != 1 else 'Bob'))


