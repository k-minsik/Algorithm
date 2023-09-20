while True:
    try:
        n = int(input())
    except:
        break

    temp = 1
    cnt = 1
    while True:
        if temp % n == 0:
            print(cnt)
            break
        else:
            temp = (temp * 10 + 1) % n
            cnt += 1