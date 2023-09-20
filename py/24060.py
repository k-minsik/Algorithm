def merge(arr):
    if len(arr) == 1:
        return arr
    
    m = (len(arr) + 1) // 2

    l = merge(arr[:m])
    r = merge(arr[m:])

    i, j = 0, 0
    temp = []

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            temp.append(l[i])
            ret.append(l[i])
            i += 1
        else:
            temp.append(r[j])
            ret.append(r[j])
            j += 1

    while i < len(l):
        temp.append(l[i])
        ret.append(l[i])
        i += 1
    
    while j < len(r):
        temp.append(r[j])
        ret.append(r[j])
        j += 1

    return temp


n, m = map(int, input().split())
data = list(map(int, input().split()))
ret = []

merge(data)
if len(ret) < m:
    print(-1)
else:
    print(ret[m-1]) 
