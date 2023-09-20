import sys
input = sys.stdin.readline

u, d, f, b, l, r = [], [], [], [], [], []
for _ in range(3):
    u.append(['w','w','w'])
    d.append(['y','y','y'])
    f.append(['r','r','r'])
    b.append(['o','o','o'])
    l.append(['g','g','g'])
    r.append(['b','b','b'])

tk = int(input())
for _ in range(tk):
    n = int(input())
    go = list(input().split())

    for s in go:
        if s == "U+":
            f[0], b[0], l[0], r[0] = r[0], l[0], f[0], b[0]
        elif s == "U-":
            f[0], b[0], l[0], r[0] = l[0], r[0], b[0], f[0]

        elif s == "D+":
            f[2], b[2], l[2], r[2] = l[2], r[2], b[2], f[2]
        elif s == "D-":
            f[2], b[2], l[2], r[2] = r[2], l[2], f[2], b[2]
        
        elif s == "F+":
            u[2], r[0][0], r[1][0], r[2][0], d[0], l[0][2], l[1][2], l[2][2] = 
            [l[0][2], l[1][2], l[2][2]], u[2][0], u[2][1], u[2][2], [r[0][0], r[1][0], r[2][0]], d[2]
        elif s == "F-":
            pass
        
        elif s == "B+":
            pass
        elif s == "B-":
            pass
        
        elif s == "L+":
            pass
        elif s == "L-":
            pass
        
        elif s == "R+":
            pass
        elif s == "R-":
            pass
        
        
