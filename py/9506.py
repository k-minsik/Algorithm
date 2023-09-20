import sys
input = sys.stdin.readline

while 1:
    a = int(input())
    if a == -1:
        break

    temp = 0
    arr = []
    for i in range(1, a//2 + 1):
        if a % i == 0:
            arr.append(i)
            temp += i

    if temp == a:
        print(a, end = " = ")
        for n in arr[:-1]:
            print(n, end = " + ")
        print(arr[-1])
    else:
        print(str(a) + " is NOT perfect.")
