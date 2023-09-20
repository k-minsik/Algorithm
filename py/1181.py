import sys
input = sys.stdin.readline

arr = []
arr2 = []

for _ in range(int(input())):
    s = input().rstrip()
    if s not in arr2:
        l = len(s)
        arr.append([s, l])
        arr2.append(s)

arr.sort(key = lambda x : (x[1], x[0]))

for i in arr:
    print(i[0])