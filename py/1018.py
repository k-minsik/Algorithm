import sys
input = sys.stdin.readline

r, c = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]
comp = ['B', 'W']

ret = 1e9
for y in range(r-7):
    for x in range(c-7):
        for i in range(2):
            cnt = 0
            idx = i
            next = comp[idx]
            for dy in range(8):
                for dx in range(8):
                    if arr[y + dy][x + dx] != next:
                        cnt += 1
                    
                    idx = (idx + 1) % 2
                    next = comp[idx]
                
                idx = (idx + 1) % 2
                next = comp[idx]
            
            ret = min(ret, cnt)

print(ret)