# n, atk = map(int, input().split())
# hp, maxHP = 0, 0

# for _ in range(n):
#     t, a, h = map(int , input().split())
    
#     if t == 1:
#         hp += a * ((h - 1)// atk)

#     elif t == 2:
#         atk += a
#         hp -= h

#     if hp < 0:
#         hp = 0
    
#     maxHP = max(maxHP, hp)

# print(maxHP + 1)


import sys
input = sys.stdin.readline

def fight(attack, HP):
    maxHp = HP

    for type, power, hp in rounds:
        if type == 1:
            count = (hp - 1) // attack
            HP -= power * count

        elif type == 2:
            attack += power
            HP = min(maxHp, HP + hp)

        if HP <= 0:
            return False
    
    return True

N, ATTACK = map(int, input().split())
rounds = []

for i in range(N):
    rounds.append(list(map(int, input().split())))

low, high = 1, int(1e18)
while low <= high:
    mid = (low + high) // 2

    if fight(ATTACK, mid):
        high = mid - 1
        answer = mid

    else:
        low = mid + 1

print(answer)