from mip import Model, maximize, BINARY, xsum
import sys

if len(sys.argv) >= 2:
    n = int(sys.argv[1])
else:
    n = int(input())

m = Model('diagonals')

l = [[m.add_var(var_type=BINARY) for i in range(n)] for j in range(n)]
r = [[m.add_var(var_type=BINARY) for i in range(n)] for j in range(n)]

m.objective = maximize(xsum(l[i][j] + r[i][j] for i in range(n) for j in range(n)))

for i in range(n):
    for j in range(n):
        m += l[i][j] + r[i][j] <= 1

for i in range(n):
    for j in range(n):
        if i > 0:
            m += l[i][j] + r[i - 1][j] <= 1
            m += r[i][j] + l[i - 1][j] <= 1
        if i < n - 1:
            m += l[i][j] + r[i + 1][j] <= 1
            m += r[i][j] + l[i + 1][j] <= 1
        if j < 0:
            m += l[i][j] + r[i][j - 1] <= 1
            m += r[i][j] + l[i][j - 1] <= 1
        if j < n - 1:
            m += l[i][j] + r[i][j + 1] <= 1
            m += r[i][j] + l[i][j + 1] <= 1
        if i > 0 and j > 0:
            m += l[i][j] + l[i - 1][j - 1] <= 1
        if i > 0 and j < n - 1:
            m += r[i][j] + r[i - 1][j + 1] <= 1
        if i < n - 1 and j > 0:
            m += r[i][j] + r[i + 1][j - 1] <= 1
        if i < n - 1 and j < n - 1:
            m += l[i][j] + l[i + 1][j + 1] <= 1

m.optimize()

total = 0

for i in range(n):
    print('|', end='')
    for j in range(n):
        if l[i][j].x >= 0.99:
            print('\|', end='')
            total += 1
        elif r[i][j].x >= 0.99:
            print('/|', end='')
            total += 1
        else:
            print(' |', end='')
    print()
print('Total {} diagonals'.format(total))
