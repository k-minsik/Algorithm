# s = input()
# b = input()
# st = []
# l = len(b)

# for i in range(len(s)):
#     st.append(s[i])

#     if ''.join(st[-l:]) == b:
#         for _ in range(l):
#             st.pop()


# if st:
#     print(''.join(st))
# else:
#     print("FRULA")

import sys
input = sys.stdin.readline

string = input().rstrip()
deleteString = input().rstrip()

stack = []
for i in range(len(string)):
    stack.append(string[i])

    if ''.join(stack[-len(deleteString):]) == deleteString:
        for _ in range(len(deleteString)):
            stack.pop()
        
if stack:
    print(''.join(stack))
else:
    print("FRULA")