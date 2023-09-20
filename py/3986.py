res = 0

n = int(input())
for _ in range(n):
    stack = []
    s = list(input().rstrip())
    stack.append(s.pop())

    while s:
        temp = s.pop()
        if stack:
            if stack[-1] == temp:
                stack.pop()
            else:
                stack.append(temp)
        else:
            stack.append(temp)
        
        
    if not stack: res += 1

print(res)

