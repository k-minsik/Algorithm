
T = int(input())
for test_case in range(1, T + 1):
    answer = 0
    string = input()
    for i in range(1, len(string)//2+2):
        if string[:i] == string[i:2*i]:
            print('#{} {}'.format(test_case, i))
            break
        elif i == len(string)//2+1:
            print('#{} {}'.format(test_case, 0))


