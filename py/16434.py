n, atk = map(int, input().split())
hp, maxHP = 0, 0

for _ in range(n):
    t, a, h = map(int , input().split())
    
    if t == 1:
        hp += a * ((h - 1)// atk)

    elif t == 2:
        atk += a
        hp -= h

    if hp < 0:
        hp = 0
    
    maxHP = max(maxHP, hp)

print(maxHP + 1)