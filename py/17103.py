tk = int(input())

mx = -1
arr = []
for _ in range(tk):
    n = int(input())
    mx = max(mx, n)
    arr.append(n)

prime = [True] * (mx + 1)
prime[0], prime[1] = False, False
for i in range(2, mx + 1):
    for j in range(i * 2, mx + 1, i):
        prime[j] = False

for i in arr:
    cnt = 0
    for j in range(i//2 + 1):
        if prime[j]:
            if prime[i-j]:
                cnt += 1
    print(cnt)
