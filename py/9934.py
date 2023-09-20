import sys
input = sys.stdin.readline

def func(s, e, level):
    mid = (s + e) // 2

    if level == k or s == e:
        temp[level-1].append(arr[mid])
        return

    temp[level-1].append(arr[mid])
    func(s, mid - 1, level + 1)
    func(mid+1, e, level + 1)


k = int(input())
arr = list(map(int, input().split()))
temp = [[] for _ in range(k)]
l = 2 ** k - 1

func(0, l, 1)

for i in temp:
    for j in i:
        print(j, end = " ")
    print()


