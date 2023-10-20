# n = int(input())

# cnt = {}
# res = ''
# for _ in range(n):
#     mem = input().strip()
#     if mem[0] in cnt:
#         cnt[mem[0]] += 1
#     else:
#         cnt[mem[0]] = 1

# cnt = dict(sorted(cnt.items(), reverse=False))
# for k, v in cnt.items():
#     if v > 4:
#         res += k

# print(res) if res else print('PREDAJA')


import sys
input = sys.stdin.readline

n = int(input())
count = [0 for _ in range(26)]

for _ in range(n):
    name = input().rstrip()
    count[ord(name[0]) - 97] += 1

ret = ""
for i in range(26):
    if count[i] >= 5:
        ret += chr(i + 97)

print(ret) if ret != "" else print("PREDAJA")