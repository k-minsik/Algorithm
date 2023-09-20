tc = int(input())

for _ in range(tc):
    bag = {}
    res = 1
    for _ in range(int(input())):
        _, what = map(str, input().split())
        if what in bag:
            bag[what] += 1
        else:
            bag[what] = 1

    for _, v in bag.items():
        res *= (v+1)

    print(res - 1)

        