n = int(input())
ret = 1
while ret < n:
    temp = ret
    for i in range(len(str(ret))):
        temp += int(str(ret)[i])

    if temp == n:
        print(ret)
        break
    ret += 1

else:
    print(0)
