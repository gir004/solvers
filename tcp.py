from math import sqrt

n = int(input())
xs = []
ys = []

for i in range(n):
    num, x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

w = []
for i in range(n):
    row = []
    for i in range(n):
        row.append(sqrt((xs[i] - xs[j]) * (xs[i] - xs[j]) + (ys[i] - ys[j]) * (ys[i] - ys[j])))
    w.append(row)


