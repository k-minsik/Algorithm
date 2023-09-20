n, b = input().split()

answer = 0
n = n[::-1]
for i in range(len(n)):
    if n[i].isalpha():
        answer += (ord(n[i]) - 55) * (int(b) ** i)
    else:
        answer += int(n[i]) * (int(b) ** i)

print(answer)
