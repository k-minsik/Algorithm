import sys
input = sys.stdin.readline

n, k = map(int, input().split())
words = [0] * n
for i in range(n):
    word = list(input().strip())

    for c in word:
        words[i] |= 1 << (ord(c) - 97)


if k < 5:
    print(0)
    exit()
elif k == 26:
    print(n)
    exit()


def count(mask):
    cnt = 0
    for word in words:
        if (word & mask) == word:
            cnt += 1
    return cnt


def dfs(c, nk, mask):
    if nk < 0:
        return 0
    if c == 26:
        return count(mask)
    
    ret = dfs(c + 1, nk, mask)
    if c not in [0, 13, 19, 8, 2]:
        ret = max(ret, dfs(c + 1, nk - 1, mask | (1 << c)))
    
    return ret


initMask = 0
for c in [0, 13, 19, 8, 2]:
    initMask |= (1 << c)

answer = dfs(0, k - 5, initMask)
print(answer)