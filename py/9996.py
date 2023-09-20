n = int(input())
s, f = input().split('*')

for _ in range(n):
    temp = input().rstrip()
    if len(temp) >= len(s) + len(f):
        if temp[0:len(s)] == s and temp[-len(f):] == f:
            print('DA')
        else:
            print('NE')
    else:
        print('NE')
