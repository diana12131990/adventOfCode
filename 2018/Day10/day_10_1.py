import re

class Point:
    def __init__(self, px, py, vx, vy):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy

    def update(self):
        self.px += self.vx
        self.py += self.vy

f = open("day_10_input.txt","r")

points = []
for line in f:
    line = line.strip()
    px, py, vx, vy = map(int, re.findall(r"-?\d+", line))
    points.append(Point(px, py, vx, vy))
f.close()


old_area = (max(p.px for p in points) - min(p.px for p in points)) * (max(p.py for p in points) - min(p.py for p in points))
while True:
    for point in points:
        point.update()
    new_area = (max(p.px for p in points) - min(p.px for p in points)) * (max(p.py for p in points) - min(p.py for p in points))
    if new_area > old_area:  # if the area starts increasing, rollback the last move and stop
        for point in points:
            point.px -= point.vx
            point.py -= point.vy
        break
    old_area = new_area
    

minx = min(p.px for p in points)
miny = min(p.py for p in points)
maxx = max(p.px for p in points)
maxy = max(p.py for p in points)
grid = [['.' for _ in range(minx, maxx+1)] for _ in range(miny, maxy+1)]
for point in points:
    grid[point.py-miny][point.px-minx] = '#'
print("\n".join("".join(row) for row in grid))
