def solution(line):
    answer = []
    points = []
    maxx, maxy = 0, 0
    minx, miny = 2001, 2001
    
    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            mom = line[i][0] * line[j][1] - line[i][1] * line[j][0]
            if mom == 0:
                continue
            
            xs = (line[i][1] * line[j][2] - line[i][2] * line[j][1]) / mom
            ys = (line[i][2] * line[j][0] - line[i][0] * line[j][2]) / mom
            if xs == int(xs) and ys == int(ys):
                xs = int(xs)
                ys = int(ys)
                points.append((xs, ys))
                maxx = max(maxx, xs)
                maxy = max(maxy, ys)
                minx = min(minx, xs)
                miny = min(miny, ys)
            
    temp = [["." for _ in range((int(maxx - minx) + 1))] for _ in range(int(maxy - miny) + 1)]
    
    points = list(set(points))
    for x, y in points:
        print(maxy - y, x - minx)
        temp[maxy - y][x - minx] = '*'

    for i in temp:
        answer.append(''.join(i))

    return answer

A = solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])

for i in A:
    print(i)
