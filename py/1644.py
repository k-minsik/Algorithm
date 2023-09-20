n = int(input())

prime = [2, 3]
for i in range(4, n + 1):
    flag = 0
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            flag = 1
            break
    if not flag:
        prime.append(i)
            
answer, l, r = 0, 0, 0
temp = prime[l]
while l <= r and r < len(prime):
    if temp == n:
        answer += 1
        temp -= prime[l]
        l += 1
    elif temp < n:
        r += 1
        if r == len(prime):
            break
        temp += prime[r]
    elif temp > n:
        temp -= prime[l]
        l += 1
    
print(answer)