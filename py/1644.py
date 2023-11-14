# n = int(input())

# prime = [2, 3]
# for i in range(4, n + 1):
#     flag = 0
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             flag = 1
#             break
#     if not flag:
#         prime.append(i)
            
# answer, l, r = 0, 0, 0
# temp = prime[l]
# while l <= r and r < len(prime):
#     if temp == n:
#         answer += 1
#         temp -= prime[l]
#         l += 1
#     elif temp < n:
#         r += 1
#         if r == len(prime):
#             break
#         temp += prime[r]
#     elif temp > n:
#         temp -= prime[l]
#         l += 1
    
# print(answer)


import sys
input = sys.stdin.readline

n = int(input())
primeNum = [2, 3]
for i in range(5, n + 1):
    valid = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            valid = False
            break

    if valid:
        primeNum.append(i)

answer = 0
s, e = 0, 0
temp = primeNum[s]
while s <= e:
    if temp == n:
        answer += 1
        e += 1
        if e == len(primeNum):
            break
        temp -= primeNum[s]
        temp += primeNum[e]
        s += 1
    
    elif temp > n:
        temp -= primeNum[s]
        s += 1

    elif temp < n:
        e += 1
        if e == len(primeNum):
            break
        temp += primeNum[e]

print(answer)