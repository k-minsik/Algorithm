# n = int(input())

# answer = []
# for _ in range(n):
#     s = input().rstrip();

#     temp = ""
#     for i in range(len(s)):
#         if s[i].isalpha():
#             if temp:
#                 answer.append(int(temp))
#                 temp = ""
#         else:
#             temp += s[i]
    
#     if temp:
#         answer.append(int(temp))

# answer.sort()

# for i in answer:
#     print(i)



import sys
input = sys.stdin.readline

num = []

n = int(input())
for _ in range(n):
    s = input().rstrip() + "e"


    temp = ""
    for i in range(len(s)):
        if s[i].isdigit():
            temp += s[i]
        else:
            if temp:
                num.append(int(temp))
                temp = ""
            
for i in sorted(num):
    print(i)