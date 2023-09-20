import sys
input = sys.stdin.readline

def func(reser):
    can = []
    start = 9
    for s, e in reser:
        if start < s:
            can.append([start, s])
        start = e
    
    if start != 18:
        can.append([start, 18])

    if len(can):
        print(len(can), "available:")
        for s, e in can:
            if s == 9:
                s = "09"
            print(str(s) + "-" + str(e))
    
    else:
        print("Not available")


n, m = map(int, input().split())
rooms = {}

for _ in range(n):
    room = input().rstrip()
    rooms[room] = []

for _ in range(m):
    room, s, e = input().split()
    rooms[room].append([int(s), int(e)])

for room, reserv in sorted(rooms.items()):
    print("Room " + room + ":")
    func(sorted(reserv))

    n -= 1
    if n != 0:
        print("-----")
