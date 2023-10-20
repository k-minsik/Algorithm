# s = input().strip()
# print(1) if s == s[::-1] else print(0)

import sys
input = sys.stdin.readline
s = input().rstrip()

print(1) if s == s[::-1] else print(0)